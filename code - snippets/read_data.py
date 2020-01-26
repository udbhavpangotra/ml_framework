`    #  read csv files

import pandas as pd 
# Find out your current working directory
import os
print(os.getcwd())

    # Read data from file 'filename.csv' 
    # (in the same directory that your python process is based)
    # Control delimiters, rows, column names with read_csv (see later) 


train = pd.read_csv("train.csv") 
test = pd.read_csv("test.csv") 
sample_submission = pd.read_csv("sample_submission.csv") 

    # Preview the first 5 lines of the loaded data 
    
print("The shape of the sample train file" + train.shape())
print("The shape of the sample test file" + test.shape())
print("The shape of the sample submission file" + sample_submission.shape())