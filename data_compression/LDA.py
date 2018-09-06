import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
df_wine=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
X,y = df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
sc=StandardScaler()
X_train_std=sc.fit_transform(X_train)
X_test_std=sc.fit_transform(X_test)
np.set_printoptions(precision=4)
mean_vecs=[]
for label in range(1,4):
    mean_vecs.append(np.mean(X_train_std[y_train==label],axis=0))

d=13
S_W=np.zeros((d,d))
for label,mv in zip(range(1,4),mean_vecs):
    class_scatter=np.cov(X_train_std[y_train==label].T)
    S_W+=class_scatter
mean_overall=np.mean(X_train_std,axis=0)
d=13
S_B=np.zeros((d,d))
for i,mean_vecs in enumerate(mean_vecs):
    n=X[y==i+1,:].shape[0]
    mean_vecs=mean_vecs.reshape(d,1)
    mean_overall=mean_overall.reshape(d,1)
    S_B+=n*(mean_vecs-mean_overall).dot((mean_vecs-mean_overall).T)
eigen_vals,eigen_vecs=np.linalg.eig(np.linalg.inv(S_W).dot(S_B))
eigen_pairs=[(np.abs(eigen_vals[i]),eigen_vecs[:,i]) for i in range(len(eigen_vals))]
eigen_pairs=sorted(eigen_pairs,key=lambda k: k[0],reverse=True)
tot=sum(eigen_vals.real)
discr=[(i/tot)for i in sorted(eigen_vals.real,reverse=True)]
cum_discr=np.cumsum(discr)
plt.bar(range(1,14),discr, alpha=0.5, align='center',label='individual "discriminability"')
plt.step(range(1,14),cum_discr,where='mid',label='cumulative "discrimiability"')
plt.ylabel('"discrimiability" ratio')
plt.xlabel('Linear Discriminants')
plt.ylim([-0.1,1.1])
plt.legend(loc='best')
plt.show()
w=np.hstack((eigen_pairs[0][1][:,np.newaxis].real,eigen_pairs[1][1][:,np.newaxis].real))
X_train_lda=X_train_std.dot(w)
color=['r','g','b']
markers=['s','x','o']
for l,c,m in zip(np.unique(y_train),color,markers):
    plt.scatter(X_train_lda[y_train==l,0],X_train_lda[y_train==l,1],c=c,label=l,marker=m)
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.legend(loc='upper right')
plt.show()