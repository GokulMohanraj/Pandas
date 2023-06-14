import pandas as pd

data = {
    "Team": ['CSK', 'MI', 'RCB', 'GT', 'SRH', 'RR'],
    "Match played": [6,5,6,7,7,5],
    "points": [10,8,12,10,8,6]
}

# Load data into a DataFrame object

df = pd.DataFrame(data)

print(df)

# Locate Row 
# Pandas use the loc attribute to return one or more specified rows

print(df.loc[2])
print(df.loc[[0,1,2]])

# Change index name 

df = pd.DataFrame(data, index=[1,2,3,4,5,6])

print(df)