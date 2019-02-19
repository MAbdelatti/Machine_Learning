import numpy as np

X = [[0, 0], [1, 1]]
Y = [0, 1]

from sklearn import svm
clf = svm.SVC()
clf.fit(X, Y)

result = clf.predict([[2, 2]])
print(result)