import numpy as np
#import matplotlib.pyplot as plt

X = [[0, 0], [1, 1]]
Y = [0, 1]

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier()
clf.fit(X, Y)

res = clf.predict([[2, 2]])

print(res)