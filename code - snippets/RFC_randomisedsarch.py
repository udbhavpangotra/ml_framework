
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV



rfc=RandomForestClassifier(random_state=42)

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]

# Number of features to consider at every split
max_features = ['auto', 'sqrt']

# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 110, num = 22)]
max_depth.append(None)

# Minimum number of samples required to split a node
min_samples_split = [2, 5, 7, 10, 15]

# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4, 6, 7, 9, 10]

# Method of selecting samples for training each tree
bootstrap = [True, False]# Create the random grid
random_grid = { 
                'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth, 
                'min_samples_split': min_samples_split,
                'min_samples_leaf': min_samples_leaf,
                'bootstrap': bootstrap
              }

print(random_grid)



# Use the random grid to search for best hyperparameters
# Random search of parameters, using 10 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, params_gird = random_grid, n_iter = 100, cv = 10, scoring = scorer, verbose=10, random_state=42, n_jobs = -1)
# Fit the random search model
rf_random.fit(X_train, y_train)



rf_random.best_params_