import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-2]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-2]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))

import datetime
from database_schemas import *
from dsstox.compounds import Compounds
from session import SQLSession
from qsar.datapoints import Datapoints
from qsar.datasets import Datasets
from qsar.dataset_datapoints import DatasetDatapoints
import os
import sys
import click
import pandas as pd
from io import StringIO

@click.command()
@click.argument('i')
@click.argument('datasetname', required=True)#, help='Highly descriptive name for the dataset')
@click.argument('username', required=True)
def cli(i, datasetname, username):
    ### HELP DOCUMENTATION ###

    """
    creates a dataset in the mysql database (qsar.datapoints, qsar.datasets, and qsar.datasetdatapoints) from a .tsv file

    input file can be .tsv, .xls or .xlsx
    if input is STDIN must be .tsv
    
    format:

    +-----------------+---------------+-----------\n
    |   DTXCID1234    |       0       | ...\n
    +-----------------+---------------+-----------\n
    |   DTXCID56789   |       1       | ...\n
    +-----------------+---------------+-----------\n


    to remove table header use tail -n +2 myfile.tsv | datatable2mysql

    """

    ####################################################################################################################

    #if not i:
    #    tsv_input = sys.stdin.read()
    #    try:
    #        myinputtable = pd.read_csv(StringIO(tsv_input), sep="\t", header=None)
    #    except:
    #        click.secho('Error: Empty Datatable', fg='red', bold=True)
    #        sys.exit(1)
    #else:
    #    try:
    #        click.secho('-- Importing {} --'.format(i), bold=True)
    #        filename, file_extension = os.path.splitext(i)
#3
    #        if file_extension == '.tsv':
     #           myinputtable = pd.read_csv(i, sep='\t', header=None)
      #      elif file_extension == '.xlsx' or file_extension == '.xls':
       #         myinputtable = pd.read_excel(i, header=None)
        #except:
         #   click.secho('Error: File Import Failed', fg='red', bold=True)
          #  sys.exit(1)
    
    #clean input table
    inputtable2 = pd.read_csv(i, sep ="\t") 
    myinputtable = inputtable2.iloc[:,0:2]
    myinputtable.columns = ['dsstox_compound_id', 'hitc']

    #QUERY database for proper ids

    mysession = SQLSession(Schemas.information_schema).get_session()

    query0 = mysession.query(Compounds.dsstox_compound_id, Compounds.id )\
        .filter(Compounds.dsstox_compound_id.in_(myinputtable.iloc[:,0]))

    mytable = pd.DataFrame(list(query0))
    mytable.columns = ['dsstox_compound_id', 'id']
    #join hitcalls
    mytable = pd.merge(myinputtable, mytable, how='inner', on=[myinputtable.columns[0], mytable.columns[0]])
    #mytable = mytable.drop(columns=['ya'])
    #mytable.columns = ['id', 'hitc']
    #make sure datatable doesn't already exist?

    def filldatasets(invitrodbdf, fd_aeid, username):
        # create a new datasets name entry
        datasets_name = str('Imported_DataTable:{}_{}'.format(fd_aeid, datetime.datetime.today().strftime("%Y%m%d")))
        description = "Imported DataTable: {} taken on the date:{}"\
            .format(fd_aeid, datetime.datetime.today().strftime("%Y%m%d"))
        datasets = Datasets(name=datasets_name, label=datasets_name,
                            updated_by=username, created_by=username,
                            long_description=description, short_description=description)
        mysession.add(datasets)
        mysession.flush()
        fk_dataset_id = int(datasets.id)

        # add datatable to the mysql database
        for index, row in invitrodbdf.iterrows():
            efk_dsstox_compound_id = row.loc['id']
            efk_chemprop_measured_property_id = None  #leave null -CG #not nullable
            measured_value_dn = row.loc['hitc']
            created_by = username
            updated_by = username

            datapoints = Datapoints(efk_dsstox_compound_id=efk_dsstox_compound_id,
                                    efk_chemprop_measured_property_id=efk_chemprop_measured_property_id,
                                    measured_value_dn=measured_value_dn,
                                    created_by=created_by,
                                    updated_by=updated_by)

            mysession.add(datapoints)
            mysession.flush()

            fk_datapoint_id = int(datapoints.id)

            dataset_datapoints = DatasetDatapoints(fk_dataset_id=fk_dataset_id,
                                                   fk_datapoint_id=fk_datapoint_id,
                                                   updated_by=username,
                                                   created_by=username)
            mysession.add(dataset_datapoints)
        mysession.commit()
    filldatasets(mytable, datasetname, username)
    ####################################################################################################################
