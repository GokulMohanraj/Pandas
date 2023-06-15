"""  Data cleaning means fixing bad data in your data set.
        Bad data could be:
        --> Empty cell
        --> Data in wrong format
        --> Wrong data
        --> Duplicates
         """

import pandas as pd

# remove rows that contain empty cells
# use argument "dropna()" to remove empty cell contained row
# this method return new DataFrame and will not change the original

df = pd.read_csv('team_details.csv')
info = df.info()
print(info)
new_df = df.dropna()

print(new_df.to_string())
print(new_df.info())

# if you want to change the original DataFrame use the "inplace = true" argument.

df1 = pd.read_csv('team_details.csv')

df1.dropna(inplace=True)

print(df1.to_string())
print(df1.info())
