from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from package_ML.ListedColormap_Iris import plot_decision_region_classification
import numpy as np
import matplotlib.pyplot as plt




iris = datasets.load_iris()
X=iris.data[:,[2,3]]
y=iris.target
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.3, random_state=0)
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
X_combined_std=np.vstack((X_train_std,X_test_std))
y_combined=np.hstack((y_train,y_test))
knn=KNeighborsClassifier(n_neighbors=5,p=1,metric='minkowski')
knn.fit(X_train_std,y_train)
plot_decision_region_classification(X_combined_std,y_combined,classifier=knn,test_idx=range(105,150))
plt.xlabel('petal length[standardized]')
plt.ylabel('petal width[stadnardized]')
plt.legend(loc='upper left')
plt.show()