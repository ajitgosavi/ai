
from sklearn import tree

# 0 is plane fruit 
# 1 is bumpy fruit
features = [[130,0],[160,1],[170,1],[120,0],[180,1]]

# 0 is apple
# 1 is orange
label = [0,1,1,0,1]

t = tree.DecisionTreeClassifier()
t = t.fit(features,label)

# You can test your prediction here
print t.predict([[110,0]])
