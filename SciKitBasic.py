
from sklearn import tree


features = [[130,0],[160,1],[170,1],[120,0],[180,1]]
label = [0,1,1,0,1]
t = tree.DecisionTreeClassifier()
t = t.fit(features,label)
print t.predict([[110,0]])
