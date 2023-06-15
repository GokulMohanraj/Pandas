import pandas as pd 

df = pd.read_csv('team_details.csv')

print(df)

df.loc[7, 'Points'] = 12
df.loc[5, 'Run rate'] = 1.23

print(df)
