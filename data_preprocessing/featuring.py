import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
df=pd.DataFrame([
    ['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.3,'class1']
                 ])
df.columns=['color','size','price','classlabel']
print(df)
#size feature의 올바른 레이블 순서를 자동으로 도출할 수 있는 편리한 함수가 없기에
#수동적으로 조율 해줘야한다
size_mapping={'XL':3,'L':2,'M':1}
df['size']=df['size'].map(size_mapping)
print(df)
class_mapping={label:idx for idx, label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)
df['classlabel']=df['classlabel'].map(class_mapping)
print(df)
'''
reverse_mapping={v:k for k, v in class_mapping.items()}
df['classlabel']=df['classlabel'].map(reverse_mapping)
print(df)
'''
X=df[['color','size','price','classlabel']].values
color_le=preprocessing.LabelEncoder()
X[:,0]=color_le.fit_transform(X[:,0])
print(X)
ohe=OneHotEncoder(categorical_features=[0])
print(ohe.fit_transform(X).toarray())
print(pd.get_dummies(df[['price','color','size']]))