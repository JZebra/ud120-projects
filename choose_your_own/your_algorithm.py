#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from time import time

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score

# clf = KNeighborsClassifier(3, weights="distance")
# training time:  0.008 s
# prediction time:  0.003 s
# accuracy is :  0.936

clf = KNeighborsClassifier(10, weights="distance")
# training time:  0.001 s
# prediction time:  0.002 s
# accuracy is :  0.94

# clf = AdaBoostClassifier(n_estimators=100, learning_rate=1)
# training time:  0.268 s
# prediction time:  0.01 s
# accuracy is :  0.924

# clf = RandomForestClassifier(n_estimators=40, max_features="auto", min_samples_split=8)
# training time:  0.13 s
# prediction time:  0.029 s
# accuracy is :  0.928

t0 = time()
clf.fit(features_train, labels_train)
print "training time: ", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time: ", round(time()-t1, 3), "s"

score = accuracy_score(pred, labels_test)
print "accuracy is : ", score

# number of features
print "feature count: ", len(features_train[0]) 

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
