import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
#print(df.head())

# 1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
filtered_df = df.iloc[::20, :][['Manufacturer', 'Model', 'Type']]
#print(new_df.head())

# 2) Replace missing values in Min.Price and Max.Price columns with their respective mean 
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

# 3) How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_100 = df[df.sum(axis=1) > 100]
#print(rows_100.head())

# 4) Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this array into two separate 2D arrays, where one represents the rows and the other represents the columns. Write a function, preferably using a lambda function, to calculate the sum of each row and each column separately, and return the results as two separate NumPy arrays
array = np.random.randint(1, 101, size=(4, 4))
print(array)

row_sums = lambda x: np.sum(x,axis= 1)
column_sums = lambda x: np.sum(x, axis=0)

row_sum = row_sums(array)
column_sum = column_sums(array)
print(row_sum, column_sum)