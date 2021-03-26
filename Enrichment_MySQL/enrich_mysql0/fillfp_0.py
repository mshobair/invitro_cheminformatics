from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.session import SQLSession
from database.qsar.compound_descriptor_sets import CompoundDescriptorSets
from database.qsar.descriptors import Descriptors
import sys
import pandas as pd
from io import StringIO


def fillfp(mytable, dsi):

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

    dsi = int(dsi)
########################################################################################################################
########################################################################################################################

    mysession1 = SQLSession(Schemas.dsstox_schema).get_session()

    # ### CHECKS FOR DTXCID IN DSSTOX.COMPOUNDS ###
    # query = mysession.query(Compounds.id, Compounds.dsstox_compound_id).filter(Compounds.dsstox_compound_id.in_(idrow))
    # df1 = pd.DataFrame(list(query))
    # df1 = [int(x) for x in df1.iloc[:, 0]]
    #
    # ### CHECKS FOR ID AND TOXPRINTS IN QSAR.COMPOUND_DESCRIPTOR_SETS ###
    # query2 = mysession.query(CompoundDescriptors.efk_dsstox_compound_id, CompoundDescriptors.descriptor_string_tsv)\
    #     .filter(CompoundDescriptors.efk_dsstox_compound_id.in_(df1))\
    #     .filter(CompoundDescriptors.fk_descriptor_set_id == 1445)

    query2 = mysession1.query(Compounds.dsstox_compound_id, CompoundDescriptorSets.descriptor_string_tsv) \
        .join(CompoundDescriptorSets, Compounds.id == CompoundDescriptorSets.efk_dsstox_compound_id) \
        .filter(CompoundDescriptorSets.fk_descriptor_set_id == dsi)

    df2 = pd.DataFrame(list(query2))
    idrow = pd.DataFrame(idrow.unique())
    idrow.columns = ['dsstox_compound_id']
    df2 = pd.merge(idrow, df2, on='dsstox_compound_id', how='inner')

    #something to separate and name fingerprint columns
    df2 = pd.concat([df2, df2['descriptor_string_tsv'].str[:].str.split('\t', expand=True)], axis=1)
    df2 = df2.drop('descriptor_string_tsv', axis=1)
    # print(df2)

    #name the columns correctly
    query3 = mysession1.query(Descriptors.descriptors_name).filter(Descriptors.fk_descriptor_set_id == dsi)
    descriptornames = list(query3)

    for num,name in enumerate(descriptornames, start=0):
        df2 = df2.rename(columns={num:name[0]})

    #creates the final output table
    mytable = mytable.rename(columns={colname : "dsstox_compound_id"})
    mytable = pd.merge(mytable, df2, on='dsstox_compound_id')
    # mytable = mytable.drop('dsstox_compound_id', 1)
    outputtable = mytable

    outputtable = outputtable.drop(outputtable.columns[-1], axis=1)

    #check for trailing column created by tab and remove
    if outputtable[outputtable.columns[-1]][0]=='':
        mytable = mytable.drop(mytable.columns[-1], axis=1)
    outputtable = mytable

    # generates a string with tab seperation and line breaks for row ends

    # columnnames = mytable.columns.values
    # output = ''
    # for i in columnnames:
    #     output += str(i) + '\t'
    # output += '\n'
    # mytable = mytable.values.tolist()
    #
    # for i in mytable:yes
    #     a = '\t'.join(str(x) for x in i)
    #     output += a + '\n'
    mysession1.close()
    return outputtable


# # # TEST # # #
if __name__ == '__main__':
    a = [['DTXCID101', 0], ['DTXCID101', 0],['DTXCID101', 1],['DTXCID202', 1],['DTXCID303',0],
         ['DTXCID404', 0],['DTXCID505',0],['DTXCID606',1],['DTXCID707',0],['DTXCID808',0],['DTXCID909',1]]
    a = pd.DataFrame(a)
    print(fillfp(a, 1445))
