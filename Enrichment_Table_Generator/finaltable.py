import pandas as pd
import scipy.stats as stats


## this only works for toxprints chemotypes can change this to work with any set of fingerprints

##create and fill final_table

def generate_final_table(my_enrichment_table,full_table):
    column_names = ['Fingerprint_ID','TP', 'FP', 'FN', 'TN', 'Odds Ratio', 'Pval']
    final_table = pd.DataFrame(index=[], columns=column_names, dtype=float)

    my_enrichment_table = my_enrichment_table.reset_index()
    my_enrichment_table = my_enrichment_table.rename(columns={'index':'Fingerprint_ID'})

    for index, row in my_enrichment_table.iterrows():
        if row['Odds Ratio'] > 3.0 and row['Pval'] < 0.05:
            final_table = final_table.append(row)
    ## create and fill total chemotypes column
    final_table.insert(1, 'F-Total', 0, allow_duplicates=False)

    for index, row in final_table.iterrows():
        final_table.loc[index, 'F-Total'] = (row['TP'] + row['FP'])
    ## create and fill balanced accuracy column
    ## accuracy column commented out
    final_table.insert(final_table.columns.get_loc("Odds Ratio"), 'Balanced Accuracy', 0.0, allow_duplicates=False)
    # final_table.insert(final_table.columns.get_loc("Odds Ratio"), 'Accuracy', 0.0, allow_duplicates=False)
    for index, row in final_table.iterrows():
        BA = (((row['TP'] / (row['TP'] + row['FN'])) + (row['TN'] / (row['TN'] + row['FP']))) / 2)
        final_table.loc[index, 'Balanced Accuracy'] = float(BA)
        #A = (((row['TP']+row['TN'])/(row['TP']+row['TP']+row['FN']+row['TN'])))
        # final_table.loc[index, 'Accuracy'] = float(A)

    ### ADD TOXPRINT IDS & CHEMOTYPE NAME ###
    # import 5-levels table
    # merge tables
    # five_levels = pd.read_excel("~/Desktop/toxprint_5levels.xlsx")
    # final_table = pd.merge(five_levels, final_table, left_on='ToxPrint_chemotype_name (original)', right_index=True)
    # five_levels['ToxPrint_chemotype_name (original)'] = five_levels['ToxPrint_chemotype_name (original)'].astype(str)

    # remove level columns   <-- can hopefully use these for hierarchy flags. Will need to clean up the file
    # reset index

    # for i in five_levels.dtypes[five_levels.columns.get_loc("Level 1"):].index:
        # final_table = final_table.drop(str(i), 1)

    # final_table = final_table.reset_index()
    # final_table = final_table.drop('index', 1)

    ### ADD CONSENSUS TOP CHEMOTYPE ROW ###
    # COMBINES ALL THE TOP CHEMOTYPES INTO 1
    # adds consensus row to final_table
    consensus_row = pd.DataFrame([['CONSENSUS ROW', 0, 0, 0, 0, 0, 0.0, 0.0, 0.0]], columns=final_table.columns)
    final_table = final_table.append(consensus_row, ignore_index=True)
    consensus_row_list = [final_table['Fingerprint_ID'][
                          :(len(final_table['Fingerprint_ID']) - 1)]]
    consensus_row_list = consensus_row_list[0]
    consensus_row_list = list(consensus_row_list)
    # consensus_row_list.append(0, endpoints)

    cut_table = full_table[consensus_row_list]
    cut_table = cut_table.sum(axis=1)
    for i, j in zip(cut_table, full_table.iloc[:,1]):
        if j == 1:
            if i > 0:
                final_table.loc[len(final_table) - 1, 'TP'] += 1
            elif i == 0:
                final_table.loc[len(final_table) - 1, 'FN'] += 1
        elif j == 0:
            if i > 0:
                final_table.loc[len(final_table) - 1, 'FP'] += 1
            elif i == 0:
                final_table.loc[len(final_table) - 1, 'TN'] += 1
        else:
            print('ERROR ' + j)

    # Adds F-Total

    final_table.loc[len(final_table) - 1, 'F-Total'] = final_table.loc[len(final_table) - 1, 'TP'] + final_table.loc[
        len(final_table) - 1, 'FP']
    # Adds OR, Pval, and Balanced accuracy for consensus row
    oddsratio, pvalue = stats.fisher_exact(
        [[final_table['TP'][len(final_table) - 1], final_table['FP'][len(final_table) - 1]],
         [final_table['FN'][len(final_table) - 1], final_table['TN'][len(final_table) - 1]]], alternative='greater')
    final_table.loc[len(final_table) - 1, 'Odds Ratio'] = oddsratio
    final_table.loc[len(final_table) - 1, 'Pval'] = pvalue
    BA = (((final_table.loc[len(final_table) - 1, 'TP'] / (
    final_table.loc[len(final_table) - 1, 'TP'] + final_table.loc[len(final_table) - 1, 'FN'])) + (
           final_table.loc[len(final_table) - 1, 'TN'] / (
           final_table.loc[len(final_table) - 1, 'TN'] + final_table.loc[len(final_table) - 1, 'FP']))) / 2)
    final_table.loc[len(final_table) - 1, 'Balanced Accuracy'] = float(BA)
    ## set integers and sig figs
    final_table[['Odds Ratio', 'Pval']] = final_table[['Odds Ratio', 'Pval']].round(decimals=3)
    final_table[['F-Total', 'TP', 'FP', 'FN', 'TN']] = final_table[['F-Total', 'TP', 'FP', 'FN', 'TN']].astype(int)

    return final_table