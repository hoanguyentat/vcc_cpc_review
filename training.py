#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kevin
#
# Created:     18/03/2017
# Copyright:   (c) kevin 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from nltk import ngrams
import numpy as np
# from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split

data = []
target_y = []
data_X = []
def readData():
	f = open("prediction.txt", "r")
	for line in f:
		line = unicode(line, 'utf8')
		data.append(line)
	f.close()
	f_target = open("target.txt", "r")
	for line in f_target:
		for x in line.split():
			target_y.append(int(x))
	f_target.close()

def training():
	knn = KNeighborsClassifier(n_neighbors=5)
	X_train = np.array(data_X)
	y_train = np.array(target_y)
	knn.fit(X_train, y_train)
	print knn.predict(data_X[0])

if __name__ == "__main__":
	readData()
	n = 3
	properties = []
	for i in xrange(len(data)):
		# n_grams = ngrams(data[i], 10)
		n_grams = [data[i][j:j+n] for j in xrange(len(data[i])-n+1)]
		# print n_grams
		for grams in n_grams:
			# print grams
			if grams not in properties:
				properties.append(grams)
	# print len(properties)
	# print target_y
	f = open("train_data.txt", "w")
	for i in xrange(0, len(data)):
		dic = ""
		data_tmp = []
		for j in xrange(0, len(properties)):
			_temp = data[i].count(properties[j])
			dic = dic + str(_temp) + " "
			data_tmp.append(_temp)
		data_X.append(data_tmp)
		f.write(dic + "\n")
	f.close()
	training()