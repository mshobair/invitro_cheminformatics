import sys
import pandas as pd
import scipy.stats as stats

def enrich(my_full_table):

    # CREATE THE ENRICHMENT TABLE
    endpoint = my_full_table.columns[1]

    row_names = my_full_table.columns[2:]
    column_names = ['CT-Total','TP', 'FP', 'FN', 'TN','Balanced Accuracy', 'Odds Ratio', 'P-val', 'Inv P-val', 'Inv OR']
    enrichment_table = pd.DataFrame(index=row_names, columns=column_names, dtype=float)
    enrichment_table = enrichment_table.fillna(value=0.0)

    def fast_fill(my_full_table):
        # large datasets enrichments are calculated much faster
        # make subsets of tables and find lengths
        tab0 = my_full_table[my_full_table[1] == 0]
        tab1 = my_full_table[my_full_table[1] == 1]
        l0 = len(tab0)
        l1 = len(tab1)
        tab0 = tab0.groupby([1]).sum()
        tab1 = tab1.groupby([1]).sum()

        count = -1
        for i in tab0.iloc[0,:]:
            count += 1
            enrichment_table['FP'][row_names[count]] = i
            enrichment_table['TN'][row_names[count]] = l0 - i

        count = -1
        for i in tab1.iloc[0,:]:
            count += 1
            enrichment_table['TP'][row_names[count]] = i
            enrichment_table['FN'][row_names[count]] = l1 - i

    def slow_fill(my_full_table):
        # this fills large datasets much more slowly but can handle empty values (dsi 1449)
        # FILL THE CONFUSION MATRIX
        for index, row in my_full_table.iterrows():
            if int(row[endpoint]) == 1:
                count = -1
                for i in row[my_full_table.columns[2]:]:
                    # i = int(i)
                    count += 1
                    if i =='':
                        pass
                    elif int(i) == 1:
                        enrichment_table['TP'][row_names[count]] += 1
                    elif int(i) == 0:
                        enrichment_table['FN'][row_names[count]] += 1
                    else:
                        print('Error')
                        sys.exit(1)
            elif int(row[endpoint]) == 0:
                count = -1
                for i in row[my_full_table.columns[2]:]:
                    # i = int(i)
                    count += 1
                    if i == '':
                        pass
                    elif int(i) == 1:
                        enrichment_table['FP'][row_names[count]] += 1
                    elif int(i) == 0:
                        enrichment_table['TN'][row_names[count]] += 1
                    else:
                        print('Error')
                        sys.exit(1)
            else:
                print(row[endpoint])
                print('ERROR: endpoint error')


    # FILL THE CONFUSION MATRIX
    #remove -1 values
    my_full_table = my_full_table.replace(-1, 0)

    # make txp values into ints
    try:
        my_full_table.iloc[:,1:] = my_full_table.iloc[:,1:].astype(int)
        fast_fill(my_full_table)
    except:
        slow_fill(my_full_table)

    # CALCULATE & FILL ODDS RATIOS & FISHER'S EXACT P-VALUES
    for index, row in enrichment_table.iterrows():
        oddsratio, pvalue = stats.fisher_exact([[row['TP'], row['FP']], [row['FN'], row['TN']]], alternative='greater')
        enrichment_table.loc[index, 'P-val'] = pvalue
        enrichment_table.loc[index, 'Odds Ratio'] = oddsratio
        enrichment_table.loc[index, 'CT-Total'] = (row['TP'] + row['FP'])
        BA = (((row['TP'] / (row['TP'] + row['FN'])) + (row['TN'] / (row['TN'] + row['FP']))) / 2)
        enrichment_table.loc[index, 'Balanced Accuracy'] = float(BA)
        inv_oddsratio, inv_pvalue = stats.fisher_exact([[row['FP'], row['TP']], [row['TN'], row['FN']]],alternative='greater')
        enrichment_table.loc[index, 'Inv P-val'] =inv_pvalue
        enrichment_table.loc[index, 'Inv OR'] = inv_oddsratio


    # ROUNDS AND SETS VALUES AS INT
    enrichment_table[['CT-Total','TP', 'FP', 'FN', 'TN']] = enrichment_table[['CT-Total','TP', 'FP', 'FN', 'TN']].astype(int)

    # create flipped endpoint statistics
    return enrichment_table


# # TEST # # #
# if __name__ == '__main__':
#     a = [['DTXCID101', 0], ['DTXCID101', 0],['DTXCID101', 1],['DTXCID202', 1],['DTXCID303',0],['DTXCID404', 0],['DTXCID505',0],['DTXCID606',1],['DTXCID707',0],['DTXCID808',0],['DTXCID909',1]]
#     from database.database_schemas import Schemas
#     from database.session import SQLSession
#     from Enrichment_MySQL.duplicate_handler_0 import handle_duplicates
#     from Enrichment_MySQL.fillfp_0 import fillfp
#     import timeit
#
#     mysession = SQLSession(Schemas.qsar_schema).get_session()
#
#     datasets = mysession.execute('SELECT ro_stg_dsstox.compounds.dsstox_compound_id, sbox_rlougee_qsar.datapoints.measured_value_dn FROM sbox_rlougee_qsar.datapoints JOIN ro_stg_dsstox.compounds ON ro_stg_dsstox.compounds.id = sbox_rlougee_qsar.datapoints.efk_dsstox_compound_id LIMIT 10000')
#
#     a = pd.DataFrame(list(datasets))
#     # a = handle_duplicates(a, 3)
#     # print(a)
#     b = fillfp(a, 1445)
#     # print(b)
#     start = timeit.default_timer()
#     c = enrich(b)
#     c.to_csv('/home/rlougee/Desktop/fastfilltest.tsv', sep='\t')
#     stop = timeit.default_timer()
#     min, sec = divmod(stop-start, 60)
#     print("TIME:", min,':', sec)
