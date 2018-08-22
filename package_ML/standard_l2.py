import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


iris = datasets.load_iris()
X=iris.data[:,[2,3]]
y=iris.target
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.3, random_state=0)
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
#
weights,parameters=[],[]
for c in np.arange(-5, 5 ,dtype=float):
    lr = LogisticRegression(C=10**c,random_state=0)
    lr.fit(X_train_std,y_train)
    weights.append(lr.coef_[1])
    parameters.append(10**c)
weights=np.array(weights)
plt.plot(parameters,weights[:,0],label='petal length')
plt.plot(parameters,weights[:,1],linestyle='--',label='petal width')
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.legend(loc='upper left')
plt.xscale('log')
plt.show()