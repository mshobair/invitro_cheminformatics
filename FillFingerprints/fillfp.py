import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-2]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-2]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))

from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.session import SQLSession
from database.qsar.compound_descriptor_sets import CompoundDescriptorSets
from database.qsar.descriptors import Descriptors
import sys
import click
import pandas as pd
from io import StringIO

@click.command()
@click.argument('cidtable', required=False)
@click.option('-o', default='',
    help='output file path in .tsv format')
@click.option('-dsi', default=1445,
    help='descriptor set id')
@click.option('-t', default=0,
    help='column headers txp=0, labels=1')
def cli(cidtable,o,dsi,t):
    ### HELP DOCUMENTATION ###

    """

    Fills rows in a .tsv containing DTXCIDs with their toxprints.
    DTXCIDs must be in index, or first two columns

    use -o ~/mypath/myfilename.tsv to export a toxprint .tsv file

    for -dsi: toxprints=1445, pubchem=1447, MACCs=1446
    a newer descriptor_set_id may be added or current dsis changed
    """

    # takes stdin if argument is not directly given

    if not cidtable:
        cidtable = sys.stdin.read()
        mytable = pd.read_csv(StringIO(cidtable), sep="\t")
    elif cidtable:
        mytable = pd.read_csv(cidtable, sep="\t")


    #checks the index, and first two columns for DTXCIDs
    #input table should be in the correct format already
    try:
        if mytable.iloc[0,0][0:6] == 'DTXCID':
            idrow = mytable.iloc[:,0]
            colname = mytable.columns.values[0]

    except:
        pass
    try:
        if mytable.iloc[0,1][0:6] == 'DTXCID':
            idrow = mytable.iloc[:,1]
            colname = mytable.columns.values[0]

    except:
        pass
    try:
        if mytable.index.values[0][0:6] == 'DTXCID':
            idrow = mytable.index.values
            mytable.index.name = 'DTXCID'
            colname = mytable.index.name
    except:
        pass


    # exit if not idrow
    # if not idrow:
    #     click.secho("DTXCID row was not found", color='red')
    # dsi = int(dsi)
########################################################################################################################
########################################################################################################################

    mysession = SQLSession(Schemas.qsar_schema).get_session()

    # ### CHECKS FOR DTXCID IN DSSTOX.COMPOUNDS ###
    # query = mysession.query(Compounds.id, Compounds.dsstox_compound_id).filter(Compounds.dsstox_compound_id.in_(idrow))
    # df1 = pd.DataFrame(list(query))
    # df1 = [int(x) for x in df1.iloc[:, 0]]
    #
    # ### CHECKS FOR ID AND TOXPRINTS IN QSAR.COMPOUND_DESCRIPTOR_SETS ###
    # query2 = mysession.query(CompoundDescriptorSets.efk_dsstox_compound_id, CompoundDescriptorSets.descriptor_string_tsv)\
    #     .filter(CompoundDescriptorSets.efk_dsstox_compound_id.in_(df1))\
    #     .filter(CompoundDescriptorSets.fk_descriptor_set_id == 1445)

    query2 = mysession.query(Compounds.dsstox_compound_id, CompoundDescriptorSets.descriptor_string_tsv) \
        .join(CompoundDescriptorSets, Compounds.id == CompoundDescriptorSets.efk_dsstox_compound_id)\
        .filter(CompoundDescriptorSets.fk_descriptor_set_id == dsi)

    df2 = pd.DataFrame(list(query2))
    idrow = pd.DataFrame(idrow)
    idrow.columns = ['dsstox_compound_id']
    df2 = pd.merge(idrow, df2, on='dsstox_compound_id', how='inner')


    # something to separate and name fingerprint columns
    df2 = pd.concat([df2, df2['descriptor_string_tsv'].str[:].str.split('\t', expand=True)], axis=1)
    df2 = df2.drop('descriptor_string_tsv', axis=1)
    # print(df2)

    # name the columns correctly
    if t == 0:
        query3 = mysession.query(Descriptors.descriptors_name).filter(Descriptors.fk_descriptor_set_id == dsi)
        descriptornames = list(query3)
    elif t == 1:
        query3 = mysession.query(Descriptors.label).filter(Descriptors.fk_descriptor_set_id == dsi)
        descriptornames = list(query3)

    for num,name in enumerate(descriptornames, start=0):
        df2 = df2.rename(columns={num:name[0]})

    # print(df2)
    # creates the final output table
    mytable = mytable.rename(columns={colname : "dsstox_compound_id"})
    mytable = pd.merge(mytable, df2, on='dsstox_compound_id')
    # mytable = mytable.drop('dsstox_compound_id', 1)

    # check for trailing column created by tab and remove
    if mytable[mytable.columns[-1]][0] == '' or mytable[mytable.columns[-1]][0] == None:
        mytable = mytable.drop(mytable.columns[-1], axis=1)
    outputtable = mytable

    # generates a string with tab seperation and line breaks for row ends
    columnnames = mytable.columns.values
    output = ''
    for i in columnnames:
        output += str(i) + '\t'
    output += '\n'
    mytable = mytable.values.tolist()

    for i in mytable:
        a = '\t'.join(str(x) for x in i)
        output += a + '\n'

    #output options
    if o =='':
        click.echo(output)
    else:
        outputtable.to_csv(o, sep='\t', index=False)

    sys.exit(0)