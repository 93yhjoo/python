import pandas as pd
import numpy as np
from package_ML.Adaline import AdalineGD
from package_ML.ListedColormap_Iris import plot_decision_region
import  matplotlib.pyplot as plt

df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',-1,1)
X=df.iloc[0:100,[0,2]].values
X_std=np.copy(X)
X_std[:,0]=(X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1]=(X[:,1] - X[:,1].mean()) / X[:,1].std()
ada = AdalineGD(n_iter=15, eta=0.01).fit(X_std, y)
ada.fit(X_std,y)
plot_decision_region(X_std,y,classifier=ada)
plt.title('Adaline-Gradient Descent')
plt.xlabel('sepal length[standardized]')
plt.ylabel('petal length[stadnardized]')
plt.legend(loc='upper left')
plt.show()
plt.plot(range(1,len(ada.cost_)+1),ada.cost_,marker='o')
plt.xlabel('Epoch')
plt.ylabel('Sum-squared-error')
plt.show()