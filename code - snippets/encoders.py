# various encoders that you can use for encoding the categorical values

import pandas as pd
import numpy as np

# label encoder

from sklearn.preprocessing import LabelEncoder

categorical_features = train.select_dtypes('object').columns


le = preprocessing.LabelEncoder()
for col in categorical_features:
    train[col] = le.fit_transform(train[col])
    
train.head()


# one hot encoder 

# column
gender = np.random.choice(['Male', 'Female', 'another'], size=size, p=[0.4, 0.4, 0.2])
train['gender'] = gender

# encoder function
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(handle_unknown='ignore', sparse=False)
oht = pd.DataFrame(ohe.fit_transform(train[['gender']]))

oht.index = train.index
num_df = train.drop(['gender'], axis=1)
train = pd.concat([num_df, oht],axis=1)


# get dummies 

pd.get_dummies(s1, dummy_na=True)

