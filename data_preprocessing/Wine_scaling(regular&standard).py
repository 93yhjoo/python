import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df.columns=['Class label','Alcohol','Malic acid','Ash','Alcalinity of ash ','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
print('Class label',np.unique(df['Class label']))
df.head()
X,y=df.iloc[:,1:].values,df.iloc[:,0].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#MinMaxScaler
mms=MinMaxScaler()
X_train_norm=mms.fit_transform(X_train)
X_test_norm=mms.transform(X_test)
#regularation
lr=LogisticRegression(penalty='l1',C=0.1)
lr.fit(X_train_norm,y_train)
print('Training accuracy(norm):',lr.score(X_train_norm,y_train))
print('Text accuracy(norm):',lr.score(X_test_norm,y_test))

#standarzation
stdsc=StandardScaler()
X_train_std=stdsc.fit_transform(X_train)
X_test_std=stdsc.transform(X_test)

#regularation
lr=LogisticRegression(penalty='l1',C=0.1)
lr.fit(X_train_std,y_train)
print('Training accuracy(std):',lr.score(X_train_norm,y_train))
print('Text accuracy(std):',lr.score(X_test_norm,y_test))

#tracking_regularation(다양한 피쳐들의 가중계수인 정규화의 경로 파악)
fig=plt.figure()
ax=plt.subplot(111)
colors=['blue','green','red','cyan','magenta','yellow','black','pink','lightgreen','lightblue','gray','indigo','orange']
weights,params=[],[]
for c in np.arange(-4,6,dtype=float):
    lr = LogisticRegression(penalty='l1', C=10**c,random_state=0)
    lr.fit(X_train_std,y_train)
    weights.append(lr.coef_[1])
    params.append(10**c)
weights=np.array(weights)
for column,color in zip(range(weights.shape[1]),colors):
    plt.plot(params, weights[:,column],label=df.columns[column+1],color=color)
plt.axhline(0,color='black',linestyle='--',linewidth=3)
plt.xlim([10**(-5),10**5])
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc='upper left')
ax.legend(loc='upper center', bbox_to_anchor=(1.2,1.03),ncol=1,fancybox=True)
plt.show()
