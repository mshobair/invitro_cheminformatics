import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-2]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-2]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))

import click
import sys
import pandas as pd
import os
from duplicatehandler import handle_duplicates
from enrichment import enrich
from finaltable import generate_final_table
from io import StringIO

@click.command()
@click.argument(i, required = False)
@click.option('-o', default='enrichment_table_result.tsv',
    help='output file in .tsv format')
@click.option('-duplicates', default=0,
    help='how to handle duplicate IDs:\n0)include duplicates\n1)discard duplicates\n2)include most frequent duplicate')
@click.option('-oenrich', default='',
              help='outputs the full enrichment table to PATH')
def cli(i ,o ,duplicates,oenrich ):

    ### HELP DOCUMENTATION ###

    """ GENERATE A TOXPRINT ENRICHMENT .tsv \n
    \n input table must have format: \n
    | Compound ID | Discrete_Endpoint | Fingerprint1 | Fingerprint2 | ...\n
    |-------------|-------------------|--------------|--------------|   \n
    | DTXCID00103 |         0         |      1       |       0      | ...\n
    |-------------|-------------------|--------------|--------------|   \n
    | DTXCID00103 |         0         |      1       |       0      | ...\n
    |-------------|-------------------|--------------|--------------|   \n
    MySQL_setup...

    STDIN must be in .tsv format
    """
    ### IMPORT FILE ###


    if not i:
        tsv_input = sys.stdin.read()
        myinputtable = pd.read_csv(StringIO(tsv_input), sep="\t")
    else:
        try:
            click.secho('-- Importing {} --'.format(i), bold=True)
            filename, file_extension = os.path.splitext(i)

            if file_extension == '.tsv':
                myinputtable = pd.read_csv(i, sep='\t')
            elif file_extension == '.xlsx' or file_extension == '.xls':
                myinputtable = pd.read_excel(i)
        except:
            click.secho('Error: File Import Failed', fg='red', bold=True)
            sys.exit(1)

    ### DUPLICATE HANDLING ###
    #add an option to set threshold for positive and negative hits?
    try:
        click.secho('-- Checking for Duplicates --', bold=True)
        myinputtable = handle_duplicates(myinputtable, duplicates)

    except:
        click.secho('Error: Duplicate Handling Failure', fg='red', bold=True)
        sys.exit(1)

    ### CONFLICTING VALUE COLUMN ###
    #ignored for now

    ### ENRICHMENT TABLE ###
    try:
        click.secho('-- Creating Full Enrichment Table --', bold=True)
        enrichment_table = enrich(myinputtable)
    except:
        click.secho('\nError: Enrichment Table Generation Failure', fg='red', bold=True)
        sys.exit(1)

    ### FINAL TABLE ###
    try:
        click.secho('\n-- Creating Finalized Table --', bold=True)
        final_table = generate_final_table(enrichment_table, myinputtable)
    except:
        click.secho('Error: Final Table Generation Failure', fg='red', bold=True)
        sys.exit(1)

    ### EXPORT TABLES ###
    click.secho('-- Exporting {} --'.format(o), bold=True)

    try:
        if oenrich == '':
            final_table.to_csv(o, sep='\t', index=False)
        else:
            enrichment_table.to_csv(oenrich, sep='\t', index=False)
            final_table.to_csv(o, sep='\t', index=False)
    except:
        click.secho('Error: Export Failure', fg='red', bold=True)
        sys.exit(1)

    click.secho('-- FINISHED --', bold=True)
