#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk import ngrams
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import re
import json

knn = KNeighborsClassifier(n_neighbors = 5)
X_train = None
X_test = None
y_train = None
y_test = None
data = []
target_y = []
data_X = []
properties = []  #array of features
n_of_grams = 3

# remove accent
def no_accent_vietnamese(s):
    # s = s.decode('utf-8')
    s = re.sub(u'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(u'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(u'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(u'[ìíịỉĩ]', 'i', s)
    s = re.sub(u'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(u'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(u'đ', 'd', s)
    return s

# Delete space, special charactor
def remove_special(s):
	s = re.sub(r'[^\x00-\x7F]+',' ', s)
	s = re.sub(r'[0-9]+','',s)
	s = re.sub(r'&[a-z]+;', '', s)
	s = re.sub(r' {1,}','', s)
	s = re.sub(r'[^a-z]+','',s)
	return s

# read data for training
def read_data(file_name):
	f = open(file_name, "r")
	for line in f:
		line = unicode(line, 'utf8')
		data.append(line)
	f.close()

#separate content
def get_furture_content(content):
	data_tmp = []
	for i in xrange(0, len(properties)):
		_temp = content.count(properties[i])
		data_tmp.append(_temp)
	return data_tmp
# read label for data training
def read_target_train():
	f_target = open("labels.txt", "r")
	for line in f_target:
		for x in line.split():
			target_y.append(int(x))
	f_target.close()

# training from data
def training():
	global y_test, X_test
	read_data("preprocessor.txt")
	read_target_train()
	# n_grams get similar document
	for i in xrange(len(data)):
		n_grams = [data[i][j:j + n_of_grams] for j in xrange(len(data[i]) - n_of_grams + 1)]
		for grams in n_grams:
			if grams not in properties:
				properties.append(grams)
	print("len properties: %d" % len(properties))
	# Get feature of each other
	for i in xrange(0, len(data)):
		dic = ""
		data_tmp = []
		for j in xrange(0, len(properties)):
			_temp = data[i].count(properties[j])
			dic = dic + str(_temp) + " "
			data_tmp.append(_temp)
		data_X.append(data_tmp)
	# sklean
	X = np.array(data_X)
	y = np.array(target_y)
	knn.fit(X, y)

	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 4)
	# knn.fit(X_train, y_train)


# predict for new sample
def prediction_data():
	data_pre = []
	with open("test/test8.json") as json_data:
		d = json.load(json_data)
		for x in d:
			# print(x)
			data_tmp = []
			content = x["categoryid2"] + x["name"] + x["description"]
			content = content.lower()
			# content = no_accent_vietnamese(content)
			# content = remove_special(content)
			content = content.encode("utf-8")
			for j in xrange(0,len(properties)):
				_temp = content.count(properties[j].encode("utf-8"))
				data_tmp.append(_temp)
			data_pre.append(data_tmp)
	pre = np.array(data_pre)
	print knn.predict(pre)
	# global y_test, X_test
	# print (y_test)
	# y_result = knn.predict(X_test)
	# print(metrics.accuracy_score(y_test, y_result))

if __name__ == "__main__":
	training()
	prediction_data()