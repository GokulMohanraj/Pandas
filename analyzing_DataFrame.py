import pandas as pd

# viewing data most used method for getting a quick overview of the DataFrame is "head()" method.

df = pd.read_csv('data.csv')

# no.of rows is not specified the head() method will return top 5 rows

print(df.head(10))

# There is also a tail() method for viewing the last rows of the DataFrame. 

print(df.tail())

# DataFrame object has a method called "info()", that gives you more information about the data set.

print(df.info())