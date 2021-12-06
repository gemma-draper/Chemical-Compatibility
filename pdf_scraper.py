#%%
import pandas as pd
import numpy as np
import camelot
import re

# read the tables from Geotech.pdf
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
def split_col_name_and_value(df):
    """
    Input: dataframe where top row values are in the form "Column_name\nValue".

    Output: dataframe with clean top row values and column names.
    """

    columns = ["Chemical"]
    
    # split top row values
    for idx in range(1, len(df.iloc[0])):
        columns.append(re.split('\n', df.iloc[0][idx])[0])
        df.iloc[0][idx] = re.split('\n', df.iloc[0][idx])[1]
    
    # create dictionary for renaming df cols
    num_list = list(range(0, len(columns)))
    col_dict = dict(zip(num_list, columns))

    # rename and reindex
    df.rename(columns=col_dict, inplace=True)
    df.index = np.arange(1, len(df)+1)

    return df

    
df0 = split_col_name_and_value(tables[0].df.iloc[12:])


full_df = df0
for i in range(1, 5):

    df = split_col_name_and_value(tables[i].df)
    full_df = pd.concat([full_df, df], ignore_index=True)

#show the data frame
full_df    
# %%


