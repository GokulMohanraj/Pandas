import pandas as pd

data_frame = {
    'Cars': ['BMW', 'Volvo', 'Ford'],
    'Passing': [3,6,5]
}

myvar = pd.DataFrame(data_frame)


if __name__ == '__main__':
   print(myvar)