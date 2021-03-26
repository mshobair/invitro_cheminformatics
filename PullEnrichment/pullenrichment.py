"""Pull Enrichments from the mysql database. You must use the full unique datasetname used with datatable2mysql.

Usage:
  pullenrichment <DataSetName> [options]

Options:
  -h, --help                  Show this screen.
  -v, --version               Shows the program version.
  -o <file>, --output <file>  Specify a new output path.
  -a, --all                   Outputs All the additional optional files
  --image                     Adds Image files for the Enrichment.
  --allassays                 Adds File showing your enriched chemotypes across all assays.
  --fpenrich                  Output Table of DTXCIDS by Enriched CT columns and adds CT model row to Enriched Stats File.
  --fullenrich                Output Enrichment data for all Toxprints.
  --OR=<n>                    Change Odds Ratio Cutoff [default: 3.0]
  --PV=<n>                    Change P-Value Cutoff [default: 0.05]
  --TP=<n>                    Change True Positives Cutoff [default: 3.0]
"""
import os, sys
newsyspath = os.path.realpath(__file__).split('\\')[:-2]
if len(newsyspath) == 0:
    newsyspath = os.path.realpath(__file__).split('/')[:-2]
    sys.path.append('/'.join(newsyspath))
else:
    sys.path.append('\\'.join(newsyspath))

from AssaySpaceIdentifier import assayspaceidentifier
from ImageMaker import imagemaker
from fpenrich import getenrichfp
from docopt import docopt
from database.database_schemas import Schemas
from database.session import SQLSession
import sys
import os
import pandas as pd
from colorama import init, Fore
import numpy as np
# initilize colorama colored CLI text
init(autoreset=True)

# turn of false positive pandas warning message
pd.options.mode.chained_assignment = None


def main():
    args = docopt(__doc__)
    # print(args)

    if args['--version']:
        print('NCCT CLI: Version 0.0.0')
        sys.exit(0)

    # set input arguments and options to variables
    DataSetName = args['<DataSetName>'].lower()
    outputpath = args['--output']
    if outputpath == None:
        outputpath = ''
    image = args['--image']
    allassays = args['--allassays']
    fullenrich = args['--fullenrich']
    fpenrich = args['--fpenrich']
    a = args['--all']
    OR = float(args['--OR'])
    PV = float(args['--PV'])
    TP = float(args['--TP'])

    if a:
        image = True
        allassays = True
        fpenrich = True

    descriptor_set_id = 1445

    # # # QUERY ENRICHMENT DATA FOR YOUR DATASETNAME # # #

    mysession = SQLSession(Schemas.qsar_schema).get_session()
    enrichment_data = mysession.execute(
        'SELECT datasets.name, descriptors.descriptors_name, descriptors.label, statistics.abbreviation, uc_statistics.value FROM sbox_rlougee_qsar.datasets JOIN sbox_rlougee_qsar.univariate_calculations ON sbox_rlougee_qsar.univariate_calculations.fk_dataset_id = sbox_rlougee_qsar.datasets.id JOIN sbox_rlougee_qsar.uc_statistics ON sbox_rlougee_qsar.uc_statistics.fk_univ_calc_id = sbox_rlougee_qsar.univariate_calculations.id JOIN sbox_rlougee_qsar.statistics ON sbox_rlougee_qsar.statistics.id = sbox_rlougee_qsar.uc_statistics.fk_statistic_id JOIN sbox_rlougee_qsar.descriptors ON sbox_rlougee_qsar.descriptors.id = sbox_rlougee_qsar.univariate_calculations.fk_descriptor_id WHERE datasets.name LIKE \'%{}%\' AND fk_descriptor_set_id = {} GROUP BY datasets.name, descriptors.descriptors_name, descriptors.label, statistics.abbreviation, uc_statistics.value'.format(DataSetName, descriptor_set_id))

    enrichment_data = pd.DataFrame(list(enrichment_data))

    if enrichment_data.empty:
        print(Fore.RED + 'ERROR: DataSetName string returned no results {}'.format(DataSetName))
        sys.exit(1)

    # format table, pivot columns, reorder
    # null columns are dropped without dropna=False but this adds empty rows
    enrichment_data = pd.pivot_table(enrichment_data, values=4, index=[0, 1, 2], columns=[3], dropna=False)
    enrichment_data = enrichment_data.reset_index(level=[0, 1, 2])
    enrichment_data.columns = ['Data Table', 'Chemotype ID', 'Chemotype Label', 'Balanced Accuracy', 'Total Chemotypes',
                     'False Negatives', 'False Positives', 'Inverse Odds Ratio', 'Inverse P-Value', 'Odds Ratio',
                     'P-Value', 'True Negatives', 'True Positives']

    # drop empty rows
    enrichment_data = enrichment_data.dropna(thresh=4)

    enrichment_data = enrichment_data[
        ['Data Table', 'Chemotype ID', 'Chemotype Label', 'Total Chemotypes', 'True Positives', 'False Positives',
         'False Negatives', 'True Negatives', 'Balanced Accuracy', 'Odds Ratio', 'P-Value', 'Inverse Odds Ratio',
         'Inverse P-Value']]

    # FIND THE BASE FOR FILE NAMES
    file_name = enrichment_data['Data Table'][0]
    file_name = file_name.split(':')[-1]

    # CREATE FOLDERS FOR RESULTS AND EDIT PATH
    if not os.path.exists(outputpath + 'CTEW_' + file_name):
        os.makedirs(outputpath + 'CTEW_' + file_name)
        outputpath = outputpath + 'CTEW_' + file_name
        os.makedirs(outputpath + '/CTEW_Results')
        os.makedirs(outputpath+ '/CTEW-INV_Results')
        regoutputpath = outputpath + '/CTEW_Results/'
        invoutputpath = outputpath + '/CTEW-INV_Results/'
    else:
        print(Fore.RED + 'ERROR: output folder {} already exists'.format(outputpath + 'CTEW_' + file_name))
        sys.exit(1)

    # # # PULL SIGNIFICANT TOXPRINTS # # #
    enrichment_data2 = enrichment_data.dropna()
    enrichment_data2.loc[:, 'Odds Ratio'] = pd.to_numeric(enrichment_data2.loc[:, 'Odds Ratio'], errors='coerce')
    enrichment_data2.loc[:, 'P-Value'] = pd.to_numeric(enrichment_data2.loc[:, 'P-Value'], errors='coerce')
    enrichment_data2.loc[:, 'True Positives'] = pd.to_numeric(enrichment_data2.loc[:, 'True Positives'], errors='coerce')

    sigtxp = []
    for i, x in enrichment_data2.iterrows():
        if x['Odds Ratio'] >= OR and x['P-Value'] <= PV and x['True Positives'] >= TP:
            sigtxp.append(x['Chemotype ID'])

    # # # PULL SIGNIFICANT INVERSE TOXPRINTS # # #
    enrichment_data3 = enrichment_data.dropna()
    enrichment_data3.loc[:, 'Inverse Odds Ratio'] = pd.to_numeric(enrichment_data3.loc[:, 'Inverse Odds Ratio'], errors='coerce')
    enrichment_data3.loc[:, 'Inverse P-Value'] = pd.to_numeric(enrichment_data3.loc[:, 'Inverse P-Value'], errors='coerce')

    invsigtxp = []
    for i, x in enrichment_data3.iterrows():
        if x['Inverse Odds Ratio'] >= OR and x['Inverse P-Value'] <= PV:
            invsigtxp.append(x['Chemotype ID'])

    # CREATE SIGNIFICANT TOXPRINT EXPORT TABLE AND INVERSE SIGNIFICANT TOXPRINT TABLE
    sigtxp = pd.DataFrame(sigtxp, columns=['Chemotype ID'])
    # sigtxp.columns = ['Chemotype ID']
    OutputTable = pd.merge(sigtxp, enrichment_data, on='Chemotype ID', how='inner')

    invsigtxp = pd.DataFrame(invsigtxp, columns=['Chemotype ID'])
    # invsigtxp.columns = ['Chemotype ID']
    InvOutputTable = pd.merge(invsigtxp, enrichment_data, on='Chemotype ID', how='inner')

    # CREATE FULL ENRICHMENT STATISTICS TABLE
    if fullenrich:
        enrichment_data.to_csv('{}Full_Enrichment_Stats_{}.tsv'.format(outputpath, file_name), sep='\t', index=False)

    # # # ENRICHED CHEMOTYPES # # #
    # return a table containing enriched chemotypes X DTXCID
    if fpenrich:
        try:
            ct_model_row = getenrichfp(DataSetName, sigtxp, regoutputpath, 'CT-Enriched_FP_'+file_name)
            OutputTable = OutputTable.append(ct_model_row)
        except:
            pass
        try:
            ct_inv_model_row = getenrichfp(DataSetName, invsigtxp, invoutputpath, 'CT-INV-Enriched_FP_' + file_name)
            InvOutputTable = InvOutputTable.append(ct_inv_model_row)
        except:
            pass

    # # # CREATE CT IMAGES # # #
    if image:
        imagemaker(sigtxp, 'CT-Enriched_Images_'+file_name, regoutputpath)
        imagemaker(invsigtxp, 'CT-INV-Enriched_Images_'+file_name, invoutputpath)

    # # # CREATE ADDITIONAL ASSAY INFO # # #
    if allassays:
        assayspaceidentifier(sigtxp, 'CT-Enriched_TCAssays_'+file_name, regoutputpath)
        assayspaceidentifier(invsigtxp, 'CT-INV-Enriched_TCAssays_'+file_name, invoutputpath)

    # # # EXPORT CT-ENRICHED_STATS & CT-INV-ENRICHED_STATS # # #
    try:
        OutputTable.to_csv('{}CT-Enriched_Stats_{}.tsv'.format(regoutputpath, file_name), sep='\t', index=False)
    except:
        pass
    try:
        InvOutputTable.to_csv('{}CT-INV-Enriched_Stats_{}.tsv'.format(invoutputpath, file_name), sep='\t', index=False)
    except:
        pass