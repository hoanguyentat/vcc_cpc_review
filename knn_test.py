#-------------------------------------------------------------------------------
# Name:        knn_test
# Purpose:
#
# Author:      kevin
#
# Created:     18/03/2017
# Copyright:   (c) kevin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
# from sklearn import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# logistic = LogisticRegression
# dir(LogisticRegression)
knn = KNeighborsClassifier(n_neighbors = 5)

print (knn)
# Luu tru cac tinh nang
X = iris.data
print X
print type(X)
# print X.shape
# Luu lai cac nhan
y = iris.target
# print y.shape
print y
print type(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 4)
# training



# hieu nang cua thuat toan
k_range = range(1,26)
scores = []
for x in k_range:
	knn.fit(X_train, y_train)
	y_result = knn.predict(X_test)
	scores.append(metrics.accuracy_score(y_test, y_result))
print len(scores)
plt.plot(k_range, scores)
plt.xlabel("x")
plt.ylabel("y")