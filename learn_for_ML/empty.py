import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from package_ML.ListedColormap_Iris import plot_decision_region_classification

np.random.seed(0)
X_xor=np.random.randn(200,2)
y_xor=np.logical_xor(X_xor[:,0]>0,X_xor[:,1]>0)
y_xor=np.where(y_xor,1,-1)
'''
plt.scatter(X_xor[y_xor==1,0],X_xor[y_xor==1,1],c='b',marker='x',label='1')
plt.scatter(X_xor[y_xor==-1,0],X_xor[y_xor==-1,1],c='r',marker='s',label='-1')
plt.ylim(-3.0)
plt.legend()
plt.show()
'''
svm=SVC(kernel='rbf',random_state=0,gamma=0.10,C=10.0)
svm.fit(X_xor,y_xor)
plot_decision_region_classification(X_xor,y_xor,classifier=svm)
plt.legend(loc='upper left')
plt.show()