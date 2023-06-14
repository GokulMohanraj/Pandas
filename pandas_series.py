import pandas as pd

# Simple pandas series from a list 

a = [1,3,5,7,9]

myvar = pd.Series(a)

print(myvar)

# Create Labels in series

label = pd.Series(a, index = ['A','B','C','D','E'])

print(label)
print(f'index value of C is:',label['C'])

# Use key/value object to create series, like dictionary

data = {'India': 345, 'England': 342, 'Australia': 321}

runs = pd.Series(data)

# key of the dictionary become the labels.
print(runs)

