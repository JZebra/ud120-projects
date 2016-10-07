#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
from sklearn.metrics import accuracy_score

# svc = svm.SVC(kernel='linear')
svc = svm.SVC(kernel='rbf', C=10000)

# only use the first 1% of training data.
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
fit = svc.fit(features_train, labels_train)
print "training time: ", round(time()-t0, 3), "s"

t1 = time()
pred = fit.predict(features_test)
print "prediction time: ", round(time()-t1, 3), "s"

score = accuracy_score(pred, labels_test)
print "accuracy is : ", score

# quiz
# idx_array = [10, 26, 50]
# for i in idx_array:
# 	print "prediction for el {0}: {1}".format(i, pred[i])

# quiz
# import numpy
# print "number of emails that belong to chris ", numpy.sum(pred)

#########################################################


# no. of Chris training emails: 7936
# no. of Sara training emails: 7884
# training time:  184.338 s
# prediction time:  19.449 s
# accuracy is :  0.984072810011

# 1% training data
# training time:  0.104 s
# prediction time:  1.151 s
# accuracy is :  0.884527872582