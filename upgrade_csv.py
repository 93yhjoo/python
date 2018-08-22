import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from sklearn.preprocessing import Imputer
'''
filename_queue=tf.train.string_input_producer(['voice.csv'],shuffle=True,name='filename_queue')

reader=tf.TextLineReader()
key,value=reader.read(filename_queue)

record_defaults=[[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],[0.],['null']]
'''
#데이터 보기
'''
file=open('orginal_voice.csv','r',encoding='utf-8')
rdr=csv.reader(file)

for line in rdr:
    print(line)
file.close()
'''
df=pd.read_csv('orginal_voice.csv')

y=df.iloc[1:101,2].values
y=np.where(y=='male',-1,1)
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