from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

rfc=RandomForestClassifier(random_state=42)

# use randomized search first and then minimise the grid search, fine tune each of these paramerters using grid search.

param_grid = { 
    'n_estimators': [64, 84, 100, 128, 200, 256, 500, 750, 1000, 1250, 1500, 2000], #The number of trees in the forest
     # when we are working with a higer number of records we should prefer using a lower number of trees and vice versa.
    'max_features': ['auto', 'sqrt', 'log2', 3, 5, 7, 9, 12], #The number of features to consider when looking for the best split
    'max_depth' : [4, 5, 6, 7, 8, 9, 10, 'None'], # The maximum depth of the tre
    'criterion' :['gini', 'entropy'], # entropy is for information gain
    'min_samples_split' :[2, 3, 4, 5], # The minimum number of samples required to split an internal node
    'class_weight' : ['balanced','balanced_subsample','None'] # use this for class imbalance 
}
# take scorer from the scoring file
scoring = scorer

CV_rfc = GridSearchCV(estimator=rfc, scoring = scorer, verbose = 10, param_grid=param_grid, cv= 10, n_jobs = -1)
CV_rfc.fit(X_train, y_train)


CV_rfc.best_params_

# an important aspect of using a Grid Search is that we should do a minimaliistic gridsearch rahter than a detailed one, this enables us to use gird search as a fine tuning method rather than a guess method.
# also, its better if we just use the major parameters first and then keep on adding a few others one after the other.
# this ensures a faster and a more robust model building.
# so for the first iteration, start with the n_estimators, max_depth and criterion for a classification problem.
