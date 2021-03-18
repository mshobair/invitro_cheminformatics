"""Chemical ID Convert will convert .tsv file columns to and from DTXCID, DTXSID, or CASRN.

Usage:
  chemidconvert <InID> <OutID> (<tsv_file>|[-]) [--help --version --output <file> --noerror]

Options:
  -h, --help                  Show this screen.
  -v, --version               Shows the program version.
  -o <file>, --output <file>  Output File (instead of stdout).
  -e, --noerror               Removes error messages.
"""
import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-2]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-2]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))

from docopt import docopt
from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.dsstox.generic_substances import GenericSubstances
from database.session import SQLSession
from database.dsstox.generic_substance_compounds import GenericSubstanceCompounds
import sys
import pandas as pd
from io import StringIO
from colorama import init, Fore
# initilize colorama colored CLI text
init(autoreset=True)

# accepted IDs
acceptedID = ['dtxcid','dtxsid', 'casrn']


def main():
    args = docopt(__doc__)
    # print(args)

    if args['--version']:
        print('NCCT CLI: Version 0.0.0')
        sys.exit(0)

    # set input arguments and options to variables
    InID = args['<InID>'].lower()
    OutID = args['<OutID>'].lower()
    tsv_input = args['<tsv_file>']
    o = args['--output']
    noerror = args['--noerror']

    # filter InID & OutID
    if InID in acceptedID:
        pass
    else:
        print(Fore.RED + 'Invalid InID: {}\n InID must be {}'.format(InID, acceptedID))
        sys.exit(1)
    if OutID in acceptedID:
        pass
    else:
        print(Fore.RED + 'Invalid InID: {}\n InID must be {}'.format(InID, acceptedID))
        sys.exit(1)

    # creates table of .tsv file
    # takes stdin if argument is not directly given
    if not tsv_input:
        tsv_input = sys.stdin.read()
        mytable = pd.read_csv(StringIO(tsv_input), sep="\t")
    elif tsv_input:
        mytable = pd.read_csv(tsv_input, sep="\t")

    # takes the chemical ID column
    idrow = mytable.iloc[:, 0]
    colname = mytable.columns.values[0]

    # make an SQL query table  for relevant SIDs & CIDs
    mysession = SQLSession(Schemas.dsstox_schema).get_session()
    query = mysession.query(GenericSubstances.dsstox_substance_id, GenericSubstances.casrn, Compounds.dsstox_compound_id)\
        .join(GenericSubstanceCompounds, GenericSubstanceCompounds.fk_generic_substance_id == GenericSubstances.id)\
        .join(Compounds, Compounds.id == GenericSubstanceCompounds.fk_compound_id)
    df = pd.DataFrame(list(query))
    df.columns = ['dtxsid', 'casrn', 'dtxcid']

    idrow = pd.DataFrame(idrow)
    idrow.columns = [InID]

    # do a join to filter out unwanted IDs
    if InID == 'dtxcid':
        df = pd.merge(idrow, df, on='dtxcid', how='inner')
    elif InID == 'casrn':
        df = pd.merge(idrow, df, on='casrn', how='inner')
    elif InID == 'dtxsid':
        df = pd.merge(idrow, df, on='dtxsid', how='inner')

    df = df.drop_duplicates(InID)

    # if no DTXCIDs returned
    if df.empty and not noerror:
        print(Fore.RED + "Error: No valid {} or no associated {}\n{}".format(InID, OutID, list(idrow)))
        sys.exit(1)
    elif df.empty:
        sys.exit(1)

    #creates a list of unconverted IDs
    noid = list(set(idrow.iloc[:,0])-set(list(df.iloc[:, 0])))

    # creates new CID table
    mytable = mytable.rename(columns={colname : InID})
    mytable = pd.merge(df, mytable, on=InID, how='left')
    for i in acceptedID:
        if i != OutID:
            mytable = mytable.drop(i, 1)
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

    # output options
    if not o:
        print(output[:int(-1)])
    else:
        outputtable.to_csv(o, sep='\t', index=False)

    # ERROR message
    # not actual STDERR this is for the user
    if not noerror:
        print(Fore.RED + "Error: Invalid {} or no associated {}\n{}".format(InID, OutID, noid))

if __name__ == '__main__':
    main()
