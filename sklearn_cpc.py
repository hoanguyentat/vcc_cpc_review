from sklearn import datasets
from sklearn import svm
import pickle

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.datam, iris.target
clf.fit(X, y)
digits = datasets.load_digits()
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',  max_iter=-1, probability=False, random_state=None, shrinking=True,  tol=0.001, verbose=False)
s = pickle.dumps(clf)
clf2 = pickle.load(s)
clf2.predict(X[0:1])
