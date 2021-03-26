"""enrich_mysql will create enrichment table data from datatables already stored in the mysql database. To add new datatables please see datatabletomysql or update_qsar_datasets. To retrieve enrichment data please see pullenrichment.

Usage:
  enrich_mysql [--help --version]

Options:
  -h, --help                  Show this screen.
  -v, --version               Shows the program version.

"""

import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-3]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-3]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))

import math
import sys
import time
from multiprocessing import Pool

import pandas as pd
from Enrichment_MySQL.enrich_mysql0.duplicate_handler_0 import handle_duplicates
from colorama import init, Fore
from docopt import docopt

from Enrichment_MySQL.enrich_mysql0.enrich import enrich
from Enrichment_MySQL.enrich_mysql0.fillfp_0 import fillfp
from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.qsar.datapoints import Datapoints
from database.qsar.dataset_datapoints import DatasetDatapoints
from database.qsar.datasets import Datasets
from database.qsar.descriptors import Descriptors
from database.qsar.uc_statistics import UcStatistics
from database.qsar.univariate_calculations import UnivariateCalculations
from database.session import SQLSession

# initilize colorama colored CLI text
init(autoreset=True)

def main():
    args = docopt(__doc__)
    # print(args)

    if args['--version']:
        print('NCCT CLI: Version 0.0.0')
        sys.exit(0)

    ### QUERY THE MYSQL DB 4 A COMPLETE LIST OF AEIDS, ENDPOINTS & DTXCIDS ###
    mysession = SQLSession(Schemas.qsar_schema).get_session()

    ### new stuff ###
    query0 = mysession.execute('SELECT DISTINCT(name) FROM sbox_rlougee_qsar.datasets WHERE id NOT IN (SELECT fk_dataset_id FROM sbox_rlougee_qsar.univariate_calculations)')
    query0 = [x[0] for x in list(query0)]

    # if query1 is empty exit
    if len(query0) == 0:
        print(Fore.RED + 'Enrichments are up to date')
        sys.exit(0)

    p = Pool(20)
    p.map(fillnewenrich, query0)


### ADD ENRICHMENTTABLE & DATATABLE TO MYSQL DATABASE
# Takes a table & a single AEID
# fills mysql uc_statistics & univariate_calculations w/ aeid, hitc, and DTXCID info

def filluc(invitrodbdf, mydatasetid):
    #set starttime
    starttime = time.time()

    username = 'rlougee'
    descriptor_set_id = [1445, 1448]
    # 1445 = toxprints
    # 1446 = MACCS
    # 1447 = pubchem
    # 1448 = Special Toxprints
    # 1449 = TOXCASTFP

    for id in descriptor_set_id:
        # add enrichment table to the mysql database
        try:
            filled_table = handle_duplicates(invitrodbdf.loc[:, ['dsstox_compound_id', 'hitc']])

        except:
            print(Fore.RED + "DUPLICATE HANDLER FAILED: {}".format(mydatasetid))
            sys.exit(1)

        try:
            filled_table = fillfp(filled_table, id)
        except:
            print(Fore.RED + "FILLFP FAILED: {}".format(mydatasetid))
            sys.exit(1)

        # filled_table = pd.DataFrame(filled_table)

        try:
            my_enrichment_table = enrich(filled_table)

        except:
            print(Fore.RED + "ENRICH FAILED: {}".format(mydatasetid))
            print(filled_table.head())
            sys.exit(1)


        # add fk_descriptor_id
        ### CHECK THAT THESE ARE MATCHING! ###
        mysession2 = SQLSession(Schemas.qsar_schema).get_session()
        query3 = mysession2.query(Descriptors.id).filter(Descriptors.fk_descriptor_set_id == id)
        query3 = list(query3)
        query3 = [int(i[0]) for i in query3]
        my_enrichment_table.insert(0, 'fk_descriptor_id', query3)

        for index, row in my_enrichment_table.iterrows():
            fk_dataset_id = int(mydatasetid)
            fk_descriptor_id = int(row['fk_descriptor_id'])

            univariate_calc = UnivariateCalculations(fk_dataset_id=fk_dataset_id,
                                                     fk_descriptor_id=fk_descriptor_id,
                                                     updated_by=username,
                                                     created_by=username)
            mysession2.add(univariate_calc)
            mysession2.flush()

            fk_univ_calc_id = int(univariate_calc.id)

            ### NEED TO CHANGE for loop & stat_list IF THE STATISTICS ARE CHANGED IN Enrichment_Table_Generator ###
            count = 0
            for i in row[1:]:

                if math.isnan(i):
                    value = None
                elif math.isinf(i):
                    value = 99999999.9
                else:
                    value = float(i)

                stat_list = [9, 10, 11, 12, 13, 4, 8, 7, 14, 15]
                fk_statistic_id = int(stat_list[count])

                uc_statistics = UcStatistics(value=value,
                                             fk_univ_calc_id=int(fk_univ_calc_id),
                                             fk_statistic_id=int(fk_statistic_id),
                                             created_by=username,
                                             updated_by=username)

                mysession2.add(uc_statistics)
                count += 1
        mysession2.commit()
        # mysession2.close()
    endtime = time.time()
    print('run time:{}'.format(endtime-starttime))

########################################################################################################################

# begin a for loop for each unique aeid
def fillnewenrich(x_aeid):
    print(x_aeid)
    # retrive the latest dataset for the aeid
    mysession = SQLSession(Schemas.qsar_schema).get_session()

    new_df = mysession.query(Compounds.dsstox_compound_id, Datapoints.measured_value_dn, Datasets.name, Datasets.id) \
        .join(Datapoints, Datapoints.efk_dsstox_compound_id == Compounds.id) \
        .join(DatasetDatapoints, Datapoints.id == DatasetDatapoints.fk_datapoint_id) \
        .join(Datasets, DatasetDatapoints.fk_dataset_id == Datasets.id)\
        .filter(Datasets.name == x_aeid)

    new_df = pd.DataFrame(list(new_df))

    # new_df = query1[query1['name'].isin([x_aeid])]
    # rename columns
    new_df.columns = ['dsstox_compound_id', 'hitc', 'name', 'dataset_id']
    my_dataset_id = new_df['dataset_id'].iloc[0]
    # make the enrichment table
    filluc(new_df, my_dataset_id)
