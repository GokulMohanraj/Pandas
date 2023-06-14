import pandas as pd 

# read_csv is used to load csv file into DataFrame

df = pd.read_csv('data.csv')

# You have large DataFrame with many rows, pandas will only return first and last 5 rows

print(df)

# Use to_string() to print the entire DataFrame

print(df.to_string())

# Using 'pd.options.display.max_rows' to check your system max rows to display

print(pd.options.display.max_rows)

# to increase the max number of rows to display the entire DF

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)