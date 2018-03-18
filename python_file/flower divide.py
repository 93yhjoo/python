Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df=pad.read_csv('https://archive.ics.uci.edu/ml' 'machine-learning-databases/iris/iris.data',hader=None)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    df=pad.read_csv('https://archive.ics.uci.edu/ml' 'machine-learning-databases/iris/iris.data',hader=None)
NameError: name 'pad' is not defined
>>> df=pd.read_csv('https://archive.ics.uci.edu/ml' 'machine-learning-databases/iris/iris.data',hader=None)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    df=pd.read_csv('https://archive.ics.uci.edu/ml' 'machine-learning-databases/iris/iris.data',hader=None)
TypeError: parser_f() got an unexpected keyword argument 'hader'
>>> df=pd.read_csv('https://archive.ics.uci.edu/ml' 'machine-learning-databases/iris/iris.data',header=None)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df=pd.read_csv('https://archive.ics.uci.edu/ml' 'machine-learning-databases/iris/iris.data',header=None)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\io\parsers.py", line 655, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\io\parsers.py", line 392, in _read
    filepath_or_buffer, encoding, compression)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\io\common.py", line 186, in get_filepath_or_buffer
    req = _urlopen(url)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\urllib\request.py", line 532, in open
    response = meth(req, response)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\urllib\request.py", line 642, in http_response
    'http', request, response, code, msg, hdrs)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\urllib\request.py", line 570, in error
    return self._call_chain(*args)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "C:\Users\joo\AppData\Local\Programs\Python\Python36\lib\urllib\request.py", line 650, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found
>>> df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
>>> df.tail()
       0    1    2    3               4
145  6.7  3.0  5.2  2.3  Iris-virginica
146  6.3  2.5  5.0  1.9  Iris-virginica
147  6.5  3.0  5.2  2.0  Iris-virginica
148  6.2  3.4  5.4  2.3  Iris-virginica
149  5.9  3.0  5.1  1.8  Iris-virginica
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> y=df.iloc[0:100,4].values
>>> y=np.where(y=='Iris-setisa',-1,1)
>>> x=df.iloc[0:100,[0,2]].values
>>> plt.scatter(x[:50,0],x[:50,1],
	    color='red',marker='o',label='setosa')
<matplotlib.collections.PathCollection object at 0x0000018998F90550>
>>> plt.scatter(x[50:100,0],x[50:100,1],
	    color='blue',marker='x',label='versicolor')
<matplotlib.collections.PathCollection object at 0x0000018998F90978>
>>> plt.xlabel('petal length')
Text(0.5,0,'petal length')
>>> plt.ylabel('sepal length')
Text(0,0.5,'sepal length')
>>> plt.legend(loc='upper left')
<matplotlib.legend.Legend object at 0x0000018998F90A20>
>>plt.show()


