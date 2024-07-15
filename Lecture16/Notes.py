"""Working with Data Using Pandas
Pandas is a powerful and flexible open-source data analysis and manipulation library for Python. It provides data structures like Series (one-dimensional) and DataFrame (two-dimensional) that are efficient for handling large datasets."""

import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Jane', 'Jim'],
    'Age': [28, 34, 29],
    'City': ['New York', 'San Francisco', 'Seattle']
}

df = pd.DataFrame(data)
print(df)
# Output:
#    Name  Age           City
# 0  John   28       New York
# 1  Jane   34  San Francisco
# 2   Jim   29        Seattle

#Creating a DataFrame from a List of Dictionaries

data = [
    {'Name': 'John', 'Age': 28, 'City': 'New York'},
    {'Name': 'Jane', 'Age': 34, 'City': 'San Francisco'},
    {'Name': 'Jim', 'Age': 29, 'City': 'Seattle'}
]

df = pd.DataFrame(data)
print(df)
# Output:
#    Name  Age           City
# 0  John   28       New York
# 1  Jane   34  San Francisco
# 2   Jim   29        Seattle

#Creating a DataFrame from a CSV File
#Assuming 'data.csv' is a CSV file in the current directory:

df = pd.read_csv('data.csv')
print(df)
print(df.head())   # Top 5 rows
print(df.tail())   # Last 5 rows
print(df.info())   # Extra information
print(df.describe())

#Selecting Columns
print(df['Name'])
print(df[['Name', 'City']])
#Filtering Rows
print(df[df['Age'] > 30])
#Adding New Columns
df['Salary'] = [55000, 65000, 75000]
print(df)
# Output:
#    Name  Age           City  Salary
# 0  John   28       New York   55000
# 1  Jane   34  San Francisco   65000
# 2   Jim   29        Seattle   75000

#Modifying Existing Columns

df['Age'] = df['Age'] + 1
print(df)
# Output:
#    Name  Age           City  Salary
# 0  John   29       New York   55000
# 1  Jane   35  San Francisco   65000
# 2   Jim   30        Seattle   75000
#Dropping Rows and Columns
df = df.drop(columns=['Salary'])
print(df)
# Output:
#    Name  Age           City
# 0  John   29       New York
# 1  Jane   35  San Francisco
# 2   Jim   30        Seattle

# Dropping a row
df = df.drop(index=1)
print(df)
# Output:
#    Name  Age     City
# 0  John   29 New York
# 2   Jim   30  Seattle
#Grouping Data
# Grouping data by a column
grouped = df.groupby('City')
print(grouped['Age'].mean())
# Output:
# City
# New York    29.0
# Seattle     30.0
# Name: Age, dtype: float64
#Aggregating Data
# Aggregating data using multiple functions
aggregated = df.groupby('City').agg({'Age': ['mean', 'min', 'max']})
print(aggregated)
# Output:
#                Age
#               mean min max
# City                      
# New York      29.0  29  29
# Seattle       30.0  30  30
#Merging DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Jane', 'Jim']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Salary': [55000, 65000, 75000]})

# Merging DataFrames on a common column
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)
# Output:
#    ID  Name  Salary
# 0   1  John   55000
# 1   2  Jane   65000
#Joining DataFrames
df1 = pd.DataFrame({'Name': ['John', 'Jane'], 'Age': [28, 34]}, index=[0, 1])
df2 = pd.DataFrame({'City': ['New York', 'San Francisco']}, index=[0, 2])

# Joining DataFrames on their index
joined_df = df1.join(df2, how='left')
print(joined_df)
# Output:
#    Name  Age           City
# 0  John   28       New York
# 1  Jane   34            NaN