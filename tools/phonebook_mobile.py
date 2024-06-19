import pandas as pd

file = "/Users/seal/Library/CloudStorage/OneDrive-Personal/share/Datasource/adhoc/NT_Phonebook.csv"
df = pd.read_csv(file, dtype=str)
df_mobile = pd.read_csv("./tools/phonebook_nt_20240619.csv", dtype=str)

# Merge to add 'มือถือ' from df2 to df1 based on 'รหัสพนักงาน'
df_merged = pd.merge(df, df_mobile[['รหัสพนักงาน', 'มือถือ']], on='รหัสพนักงาน', how='left')

# Display the merged dataframe
print(df_merged)
print(df_merged.columns)


df_merged.to_csv("./tools/NT_Phonebook.csv", index=False)