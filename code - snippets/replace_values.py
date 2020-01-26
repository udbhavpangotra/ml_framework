import pandas as pd
import numpy as np


# Replace missing values with a number
cols = []
value = 1234
train.cols.fillna(value, inplace=True)'

# Location based replacement
cols = []
train.loc[2,cols] = 125

# Replace using median 
cols = []
median = train.cols.median()
train.cols.fillna(median, inplace=True)

# Replace using mode
cols = []
mode = train.cols.mode()
train.cols.fillna(mode, inplace=True)

# Replace using mean
cols = []
mean = train.cols.mean()
train.cols.fillna(mean, inplace=True)

# This will replace "Boston Celtics" with "Omega Warrior" 
train.replace(to_replace ="Boston Celtics", value ="Omega Warrior") 

# This will replace "Boston Celtics" and "Texas" with "Omega Warrior" 
train.replace(to_replace =["Boston Celtics", "Texas"], value ="Omega Warrior") 


# Will replace  Nan value in dataframe with value -99999  
train.replace(to_replace = np.nan, value =-99999) 


# Replace all values of -999 with NAN
train.replace(-999, np.nan)


# Replace multiple values with corresponding values
train.replace({25:26,'john':'johnny'})


# Replace in a single column
train.replace({'num_pets':{0:1}})
