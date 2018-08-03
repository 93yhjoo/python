import matplotlib.pyplot as plt
import  numpy as np
import pandas as pd
from package_ML.Adaline import AdalineGD
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',-1,1)
#iloc은 index,column 값 범위를 숫자만 받는다
X=df.iloc[0:100,[0,2]].values
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
#learning_rate=0.01 difuusion
ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
ax[0].plot(range(1, len(ada1.cost_)+1),np.log10(ada1.cost_),marker='o')
ax[0].set_xlabel('Epoches')
ax[0].set_ylabel('log(sum-squared-error)')
ax[0].set_title('Adaline -learning rate 0.01')
#learning_rate=0.01 collect
ada2=AdalineGD(n_iter=10,eta=0.0001).fit(X,y)
ax[1].plot(range(1, len(ada2.cost_)+1),ada2.cost_,marker='o')
ax[1].set_xlabel('Epoches')
ax[1].set_ylabel('sum-squared-error')
ax[1].set_title('Adaline -learning rate 0.0001')
plt.show()

