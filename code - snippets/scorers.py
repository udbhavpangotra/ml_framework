from sklearn.metrics import  make_scorer
sklearn.metrics.make_scorer(score_func, greater_is_better=True, needs_proba=False, needs_threshold=False, **kwargs)


# accuracy score
from sklearn.metrics import  make_scorer
from sklearn.metrics import accuracy_score

sklearn.metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)
accuracy_score(y_true, y_pred)

scorer = make_scorer(accuracy_score, normalize = False)


# Area under the curve
from sklearn.metrics import  make_scorer
from sklearn.metrics import auc

auc_score = auc(x, y)

scorer = make_scorer(auc_score)



# average precision score
from sklearn.metrics import  make_scorer
from sklearn.metrics import average_precision_score

sklearn.metrics.average_precision_score(y_true, y_score, average='macro', pos_label=1, sample_weight=None)

precision_score = average_precision_score(y_true, y_pred, average = 'macro',multi_class= 'raise')

# chose from one of these for the average key
average = ['micro','macro','weighted','samples']
multi_class = ['raise', 'ovr', 'ovo']   

scorer = make_scorer(precision_score)


# balanced accuracy score
from sklearn.metrics import  make_scorer
from sklearn.metrics import balanced_accuracy_score

sklearn.metrics.balanced_accuracy_score(y_true, y_pred, sample_weight=None, adjusted=False)

balanced_accuracy = balanced_accuracy_score(y_true, y_pred)

make_scorer(balanced_accuracy)