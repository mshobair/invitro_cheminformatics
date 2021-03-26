import pandas as pd
import sys, os

# input significant toxprints ,and return a table containing all assay these toxprints were significant in
def assayspaceidentifier(SigTXP, myfilename, mypath=''):
    if len(SigTXP) == 0:
        return None

    path = os.path.realpath(__file__).split('\\')[:-1]
    if len(path) == 0:
        path = os.path.realpath(__file__).split('/')[:-1]
        path = '/'.join(path) + '/ENRICHMENTS_invitrodb_v3_1_BASELINE_hitc_MC_2019.tsv'
    else:
        path = '\\'.join(path) + '\\ENRICHMENTS_invitrodb_v3_1_BASELINE_hitc_MC_2019.tsv'

    AAF = pd.read_csv(path, sep='\t')
    SigTXP = pd.DataFrame(SigTXP)
    SigTXP.columns = ['descriptors_name']
    OutputTable = pd.merge(SigTXP, AAF, on='descriptors_name', how='inner')
    OutputTable.columns = ['Chemotype ID', 'Data Table', 'Chemotype Label',	'Total Chemotypes',	'True Positives', 'False Positives', 'False Negatives', 'True Negatives',	'Balanced Accuracy', 'Odds Ratio', 'P-Value', 'Inverse Odds Ratio',	'Inverse P-Value']
    OutputTable['Total Chemicals'] = OutputTable['Total Chemotypes'] + OutputTable['False Negatives'] + OutputTable['True Negatives']
    OutputTable['Hit Rate %'] = round(OutputTable['Total Chemotypes']/OutputTable['Total Chemicals'],2) * 100
    OutputTable.to_csv('{}{}.tsv'.format(mypath, myfilename), sep='\t', index=False)

# # # TEST # # #
if __name__ == '__main__':
    assayspaceidentifier(['Txp-1', 'Txp-2', 'Txp-3'], 'MY_TEST_FILE')