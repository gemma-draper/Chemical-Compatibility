#%%
import pandas as pd
import numpy as np
import camelot
import re

# read the tables from pdf
tables = camelot.read_pdf(
    'resources\pdfs\Geotech.pdf', 
    pages='all',
    flavor="stream",
    edge_tol=500
    )
print(tables)

for i in range(len(tables)):
    print(tables[i].parsing_report)
    

# get the table key 
key_dict = {}
for item in pd.concat([
    tables[0].df.head(11)[0].iloc[2:9],
    tables[0].df.head(11)[3].iloc[2:5],
    tables[0].df.head(11)[3].iloc[7:9]
]):

    try:
        k = re.split(' = | >| <', item)[0]
        v = re.split(' = | >| <', item)[1]
        key_dict[k] = v
    except IndexError:
        continue

print(f"Key: {key_dict}")

# split the top row into col names and value
columns = ["Chemical"]
df0 = tables[0].df.iloc[12:]
for idx in range(1, len(df0.iloc[0])):
    columns.append(re.split('\n', df0.iloc[0][idx])[0])
    df0.iloc[0][idx] = re.split('\n', df0.iloc[0][idx])[1]

#%%
# create dictionary for renaming df cols
num_list = list(range(0, len(columns)))
col_dict = dict(zip(num_list, columns))

# rename and reindex
df0.rename(columns=col_dict, inplace=True)
df0.index = np.arange(1, len(df0)+1)

# %%
