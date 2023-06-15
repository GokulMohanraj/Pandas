import pandas as pd

df_original = pd.read_csv('team_details.csv')
print(df_original)

# Insert value to any empty cell using "mean()"

df_mean = pd.read_csv('team_details.csv')

# Using .mean() method Mean = sum of all values divided by number of values in the columns. 
x = df_mean['Points'].mean()

df_mean['Points'].fillna(x, inplace=True)

print(df_mean)

# Insert value to any empty cell using "median()"

df_median = pd.read_csv('team_details.csv')

# Using .median() method Median = the value in the middle, after you stored all values ascending.
x = df_median['Points'].median()
df_median['Points'].fillna(x, inplace=True)
print(df_median) 

# Insert value to any empty cell using "mode()"

df_mode = pd.read_csv('team_details.csv')

# Using .mode() method Mode = the value that appears most frequently. 
# If there are multiple mode values, it returns all of them. By using [0], you are accessing the first value in the mode Series.
x = df_mode['Points'].mode()[0]
#print(x)
df_mode['Points'].fillna(x, inplace=True)

print(df_mode)