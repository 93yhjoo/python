import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  MinMaxScaler
from sklearn.linear_model import LogisticRegression

#데이터 보기

df=pd.read_csv('voice.csv')
df.columns=['meanfreq','sd','median','Q25','Q75','IQR','skew','kurt','sp.ent','sfm','mode','centroid','meanfun','minfun','maxfun',
            'meandom','mindom','maxdom','dfrange','modindx','label']
print('label',np.unique(df['label']))
#테스트,훈련용 분할
X,y=df.iloc[1:,:20].values,df.iloc[1:,20].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#스케일링 평균0 분산 1이 되도록 만들어 오버플로우 언더플로우 방지 공분산 행렬의 조건수 감소 최적화 안정성 수렴 속도 향상
mms=MinMaxScaler()
X_train_norm=mms.fit_transform(X_train)
X_test_norm=mms.fit_transform(X_test)
#희소 솔루션
lr=LogisticRegression(penalty='l1',C=0.1)
lr.fit(X_train_norm,y_train)
print('train accuracy:', lr.score(X_train_norm,y_train))
print('test accuracy:',lr.score(X_test_norm,y_test))
print(lr.intercept_)
print(lr.coef_)
#정규화 강도 경로:문제점 원 핫 인코딩 안됨...
fig=plt.figure()
ax=plt.subplot(111)
colors=['blue','green','red','cyan','magenta','yellow','black','pink','lightgreen','lightblue','gray','indigo','orange']
weights,params=[],[]
for c in np.arange(-4,6,dtype=float):
    lr = LogisticRegression(penalty='l1', C=10**c,random_state=0)
    lr.fit(X_train_norm,y_train)
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

y=df.iloc[1:101,2].values
X=df.iloc[1:101,[0,2]].values
#원본 데이터 분포도 보기
plt.scatter(X[:50,0],X[:50,1],color='red',marker='o',label='male')
plt.scatter(X[50:100,0],X[50:100,1],color='blue',marker='x',label='female')
plt.xlabel('meanfreq')
plt.ylabel('sd')
plt.show()

#데이터 정확도 높이기
#결측값 보정
imr=Imputer(missing_values=0,strategy='mean',axis=1)


#학습 데이터

#실전 데이터

#보이기
plt.scatter(X[:50,0],X[:50,1],color='red',marker='o',label='male')
plt.scatter(X[50:100,0],X[50:100,1],color='blue',marker='x',label='female')
plt.xlabel('meanfreq')
plt.ylabel('sd')
plt.show()