from sklearn.svm import SVC
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
#svm=SVC(kernel='linear',C=1.0, random_state=0)
#gamma값을 통해 경계를 조정할 수 있다.
svm=SVC(kernel='rbf',C=1.0, random_state=0,gamma=0.2)
svm.fit(X_train_std,y_train)

plot_decision_region_classification(X_combined_std,y_combined,classifier=svm,test_idx=range(105,150))
plt.xlabel('petal length[standardized]')
plt.ylabel('petal width[stadnardized]')
plt.legend(loc='upper left')
plt.show()