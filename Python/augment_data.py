import pandas as pd
import numpy as np
import os

# Read in the data
df = pd.read_csv('../Data/data.csv')

# show first 5 rows

print(df.head())

# show last 5 rows

print(df.tail())


# show the shape of the Data
print(df.shape)
# show the columns
print(df.columns)
# show the data types
print(df.dtypes)

