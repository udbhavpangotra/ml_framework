# print the first file rows in the training file
import pandas as pd
import numpy as np


print(train.head())


# Any missing values?
print(train.isnull().values.any())


# Total number of missing values
print(train.isnull().sum().sum())


# print the total null values in the training set for each column
print(train.isna().sum())


# print the total null values that exist in the specified columns for a dataset
cols = []
print(train.cols.isna().sum())


# various formats of missing values that can exist
# use this code then and remove them in the loading itself
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property data.csv", na_values = missing_values)