from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
iris = load_iris()

test_indexs = [0,50,100]


# Training datasets

train_target = np.delete(iris.target, test_indexs)
train_data = np.delete(iris.data , test_indexs, axis = 0)

# testing data

testing_target = iris.target[test_indexs]
testing_data = iris.data[test_indexs]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print testing_target

print clf.predict(testing_data)
