import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-2]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-2]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))
from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.dsstox.generic_substances import GenericSubstances
from database.session import SQLSession
from database.dsstox.generic_substance_compounds import GenericSubstanceCompounds
import sys
import click
import pandas as pd
from io import StringIO

@click.command()
@click.argument('tsv_input', required=False)
@click.option('-o', default='',
    help='output file path in .tsv format')
@click.option('-noerror', is_flag=True, default=True,
    help='remove the default error message')
def cli(tsv_input,o,noerror):
    ### HELP DOCUMENTATION ###

    """
    SIDtoCID takes in a .tsv datatable with a dsstox_substance_id column (must be index or first 2 columns).
    The dsstox_substance_id column is converted to dsstox_compound_id.
    Can use a .tsv file as stdin. Default output is stdout as .tsv.
    \n\n
    Warning!: column names are needed in the input .tsv! Otherwise first row will be skipped.



    -- EXAMPLE I/O TABLES --

    INPUT:  .tsv file

    |DTXSID COLUMN | ENDPOINT COLUMN |\n
    ----------------------------------\n
    | DTXSID123456 |        0        |\n
    ----------------------------------\n
    | DTXSID234567 |        1        |\n
    ----------------------------------\n
    | DTXSID345678 |        0        |\n
    ----------------------------------\n

    EXPORT: .tsv file

    |DTXCID COLUMN | ENDPOINT COLUMN |\n
    ----------------------------------\n
    | DTXCID891011 |        0        |\n
    ----------------------------------\n
    | DTXCID910111 |        1        |\n
    ----------------------------------\n
    | DTXCID101112 |        0        |\n
    ----------------------------------\n



    """
    # creates table of .tsv file
    # takes stdin if argument is not directly given
    if not tsv_input:
        tsv_input = sys.stdin.read()
        mytable = pd.read_csv(StringIO(tsv_input), sep="\t")
    elif tsv_input:
        mytable = pd.read_csv(tsv_input, sep="\t")

    #checks the index, and first two columns for DTXSIDs
    #input table should be in the correct format already
    try:
        if mytable.iloc[0,0][0:6] == 'DTXSID':
            idrow = mytable.iloc[:,0]
            colname = mytable.columns.values[0]

    except:
        pass
    try:
        if mytable.iloc[0,1][0:6] == 'DTXSID':
            idrow = mytable.iloc[:,1]
            colname = mytable.columns.values[0]

    except:
        pass
    try:
        if mytable.index.values[0][0:6] == 'DTXSID':
            idrow = mytable.index.values
            mytable.index.name = 'DTXSID'
            colname = mytable.index.name
    except:
        pass

    # drop empty columns
    mytable = mytable.dropna(axis='columns', how='all')

    # click.echo(mytable.columns.values)
    #make an SQL query table  for relevant SIDs & CIDs
    mysession = SQLSession(Schemas.dsstox_schema).get_session()

    query = mysession.query(GenericSubstances.dsstox_substance_id, Compounds.dsstox_compound_id).join(GenericSubstanceCompounds) \
        .join(Compounds)

    df = pd.DataFrame(list(query))
    idrow = pd.DataFrame(idrow)
    idrow.columns = ['dsstox_substance_id']
    df = pd.merge(idrow, df, on='dsstox_substance_id', how='inner')


    #if no DTXCIDs returned
    if df.empty and noerror:
        click.secho("Error: No valid DTXSIDs or no associated DTXCIDs\n{}".format(list(idrow)), fg='red', bold=True)
        sys.exit(1)
    elif df.empty:
        sys.exit(1)

    #creates new CID table
    mytable = mytable.rename(columns={colname : "dsstox_substance_id"})
    mytable = pd.merge(df, mytable, on='dsstox_substance_id')
    mytable = mytable.drop('dsstox_substance_id', 1)
    outputtable = mytable

    # generates a string with tab seperation and line breaks for row ends
    columnnames = mytable.columns.values
    output = ''
    for i in columnnames:
        output += i + '\t'
    output += '\n'
    mytable = mytable.values.tolist()

    for i in mytable:
        a = '\t'.join(str(x) for x in i)
        output += a + '\n'

    #output options
    if o =='':
        click.echo(output)
    else:
        outputtable.to_csv(o, sep='\t',index=False)

    # get IDs that were not converted
    noid = list(list(set(idrow.iloc[:,0]) - set(df.iloc[:,0])))

    #ERROR message
    #not actual STDERR this is for the user
    if noerror:
        click.secho("Error: Invalid DTXSID or no associated DTXCID\n{}".format(noid), fg='red', bold=True)

