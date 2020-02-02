from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

rfc=RandomForestClassifier(random_state=42)

# use randomized search first and then minimise the grid search, fine tune each of these paramerters using grid search.

param_grid = { 
    'n_estimators': [100, 200, 500, 750, 1000, 1250, 1500, 2000], #The number of trees in the forest
    'max_features': ['auto', 'sqrt', 'log2', 3, 5, 7, 9], #The number of features to consider when looking for the best split
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