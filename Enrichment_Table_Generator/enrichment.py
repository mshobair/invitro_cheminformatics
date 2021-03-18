import progressbar
import pandas as pd
import scipy.stats as stats
import click

def enrich(my_full_table):
    # CREATE THE ENRICHMENT TABLE
    endpoint = my_full_table.columns[1]
    row_names = my_full_table.columns[2:]
    column_names = ['TP', 'FP', 'FN', 'TN', 'Odds Ratio', 'Pval']
    enrichment_table = pd.DataFrame(index=row_names, columns=column_names, dtype=float)
    enrichment_table = enrichment_table.fillna(value=0.0)
    # PROGRESS BAR
    bar = progressbar.ProgressBar(max_value=(len(my_full_table[:])))
    # FILL THE CONFUSION MATRIX
    for index, row in my_full_table.iterrows():
        #progress bar update
        bar.update(index+1)
        if int(row[endpoint]) == 1:
            count = -1
            for i in row[my_full_table.columns[2]:]:
                count += 1
                if i == 1:
                    enrichment_table['TP'][row_names[count]] += 1
                elif i == 0:
                    enrichment_table['FN'][row_names[count]] += 1
        elif int(row[endpoint]) == 0:
            count = -1
            for i in row[my_full_table.columns[2]:]:
                count += 1
                if i == 1:
                    enrichment_table['FP'][row_names[count]] += 1
                elif i == 0:
                    enrichment_table['TN'][row_names[count]] += 1
        else:
            print('ERROR: ', index, row)
    # CALCULATE & FILL ODDS RATIOS & FISHER'S EXACT P-VALUES

    for index, row in enrichment_table.iterrows():
        oddsratio, pvalue = stats.fisher_exact([[row['TP'], row['FP']], [row['FN'], row['TN']]], alternative='greater')
        enrichment_table.loc[index, 'Pval'] = pvalue
        enrichment_table.loc[index, 'Odds Ratio'] = oddsratio

    # ROUNDS AND SETS VALUES AS INT
    # enrichment_table = enrichment_table.sort_values(by=['TP'], ascending=False)

    enrichment_table[['Odds Ratio', 'Pval']] = enrichment_table[['Odds Ratio', 'Pval']].round(decimals=3)
    enrichment_table[['TP', 'FP', 'FN', 'TN']] = enrichment_table[['TP', 'FP', 'FN', 'TN']].astype(int)
    return enrichment_table