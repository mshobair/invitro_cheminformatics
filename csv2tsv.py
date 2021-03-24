import pandas as pd
import glob


for f in glob.glob('/home/mshobair/new/invitro_cheminformatics/clean/*'):
    a = pd.read_csv(f)
    b = f.split('.csv')[0]
    b = b.split('/')[-1]
    # print(b)
    a.to_csv('/home/mshobair/new/invitro_cheminformatics/tsv/{}.tsv'.format(b), sep='\t', index=False)

