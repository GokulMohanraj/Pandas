import pandas as pd 

df = pd.read_csv('team_details.csv')
print(df)

# duplicated() can return the boolean value return TRUE means that row is duplicate otherwise FALSE 
print(df.duplicated())

# drop_duplicates() method is used to remove duplicate rows 
df.drop_duplicates(inplace=True)

print(df)