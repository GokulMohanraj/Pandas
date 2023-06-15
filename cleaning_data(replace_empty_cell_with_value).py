import pandas as pd 

# Replace empty values
# Argument "fillna()" method used to replace the empty cell with value. 

df_original = pd.read_csv('team_details.csv')

df_modified = pd.read_csv('team_details.csv')

df_modified.fillna(10, inplace=True)

print(df_original)
print(df_modified)

# Replace only for special columns

df = pd.read_csv('team_details.csv')
df['Points'].fillna(10, inplace=True)
print(df)