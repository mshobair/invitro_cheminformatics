from database.database_schemas import Schemas
from database.dsstox.compounds import Compounds
from database.session import SQLSession
from database.qsar.compound_descriptor_sets import CompoundDescriptorSets
from database.qsar.descriptors import Descriptors
import sys
import pandas as pd
from io import StringIO
import scipy.stats as stats


def getenrichfp(DataSetName, sigtxp, mypath, myfilename, dsi=1445):
    """ Get Enrichment data for a combined set of chemotypes """

    # aborts if no significant chemotypes
    if len(sigtxp) == 0:
        return None

    mysession = SQLSession(Schemas.qsar_schema).get_session()
    MyDataSet = mysession.execute(
        'SELECT dsstox_compound_id, measured_value_dn, descriptor_string_tsv FROM sbox_rlougee_qsar.datasets'
        ' JOIN sbox_rlougee_qsar.dataset_datapoints ON sbox_rlougee_qsar.dataset_datapoints.fk_dataset_id = sbox_rlougee_qsar.datasets.id'
        ' JOIN sbox_rlougee_qsar.datapoints ON sbox_rlougee_qsar.datapoints.id = sbox_rlougee_qsar.dataset_datapoints.fk_datapoint_id'
        ' JOIN ro_stg_dsstox.compounds ON sbox_rlougee_qsar.datapoints.efk_dsstox_compound_id = ro_stg_dsstox.compounds.id'
        ' JOIN sbox_rlougee_qsar.compound_descriptor_sets ON ro_stg_dsstox.compounds.id = sbox_rlougee_qsar.compound_descriptor_sets.efk_dsstox_compound_id'
        ' WHERE sbox_rlougee_qsar.datasets.name LIKE \'%{}%\' AND sbox_rlougee_qsar.compound_descriptor_sets.fk_descriptor_set_id = {}'.format(DataSetName, dsi))
    MyDataSet = pd.DataFrame(list(MyDataSet))

    MyDataSet.columns = ['Dsstox_Compound_ID', 'Hit_Call', 'Toxprint']

    #something to separate and name fingerprint columns
    MyDataSet = pd.concat([MyDataSet, MyDataSet['Toxprint'].str[:].str.split('\t', expand=True)], axis=1)
    MyDataSet = MyDataSet.drop('Toxprint', axis=1)

    #name the columns correctly
    query3 = mysession.query(Descriptors.descriptors_name, Descriptors.label).filter(Descriptors.fk_descriptor_set_id == dsi)
    descriptornames = pd.DataFrame(list(query3))

    for num,name in enumerate(descriptornames['label'], start=0):
        MyDataSet = MyDataSet.rename(columns={num:name})

    # drop columns that are not significant
    sigtxp = pd.DataFrame(sigtxp)
    sigtxp.columns = ['descriptors_name']
    siglabel = pd.merge(sigtxp, descriptornames, on='descriptors_name', how='inner')
    siglabel = list(siglabel['label'])

    for i in MyDataSet.columns[2:]:
        if i in siglabel:
            pass
        else:
            MyDataSet = MyDataSet.drop(i, axis=1)

    MyDataSet.to_csv('{}{}.tsv'.format(mypath, myfilename), sep='\t', index=False)

    # return overall balanced accuracy calculations
    # can just make a unique confusion matrix for significant toxprints and add to CT-Enriched Stats file
    # print(MyDataSet.head())
    model_row = pd.DataFrame([['Chemotype Full Model Coverage', myfilename, " ".join(sigtxp['descriptors_name']), 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0]], columns = ['Chemotype ID','Data Table','Chemotype Label','Total Chemotypes','True Positives','False Positives','False Negatives','True Negatives','Balanced Accuracy','Odds Ratio','P-Value','Inverse Odds Ratio','Inverse P-Value'])

    # fill model_row confusion matrix
    for index, row in MyDataSet.iterrows():
        rowsum = sum([int(x) for x in row.iloc[2:]])
        if row['Hit_Call'] == 1 and rowsum > 0:
            model_row['True Positives'] += 1
        elif row['Hit_Call'] == 1 and rowsum == 0:
            model_row['False Negatives'] += 1
        elif row['Hit_Call'] == 0 and rowsum > 0:
            model_row['False Positives'] += 1
        elif row['Hit_Call'] == 0 and rowsum == 0:
            model_row['True Negatives'] += 1

    # fill model_row statistics
    oddsratio, pvalue = stats.fisher_exact([ [int(model_row['True Positives']), int(model_row['False Positives'])], [int(model_row['False Negatives']), int(model_row['True Negatives'])]], alternative='greater')
    model_row['P-Value'] = pvalue
    model_row['Odds Ratio'] = oddsratio
    model_row['Total Chemotypes'] = (model_row['True Positives'] + model_row['False Positives'])
    BA = (((model_row['True Positives'] / (model_row['True Positives'] + model_row['False Negatives'])) + (model_row['True Negatives'] / (model_row['True Negatives'] + model_row['False Positives']))) / 2)
    model_row['Balanced Accuracy'] = float(BA)
    inv_oddsratio, inv_pvalue = stats.fisher_exact([ [int(model_row['False Positives']), int(model_row['True Positives'])], [int(model_row['True Negatives']), int(model_row['False Negatives'])] ],alternative='greater')
    model_row['Inverse P-Value'] = inv_pvalue
    model_row['Inverse Odds Ratio'] = inv_oddsratio

    # print(model_row)
    return model_row

# # # # TEST # # #
# if __name__ == '__main__':
#     getenrichfp('%pod%ratio%v5%',['Txp-1', 'Txp-2', 'Txp-541'] ,'~/Desktop/','TEST', 1445)
