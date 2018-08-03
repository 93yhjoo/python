import os
import struct
import numpy as np


def load_mnist(path,kind='train'):
    labels_path=os.path.join(path,'%s-labels-idx1-ubyte' %kind)
    images_path = os.path.join(path, '%s-labels-idx3-ubyte' % kind)

    with open(labels_path,'rb') as lbpath:
        magic,n=struct.unpack(">II",lbpath.read(8))
        labels=np.fromfile(lbpath,dtype=np.uint8)
    with open(images_path,'rb') as imgpath:
        magic,num,rows,cols=struct.unpack(">IIII",images_path.read(16))
        images=np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels),784)

    return images,labels


X_train,y_train=load_mnist('MNIST_data',kind='train')
print('Row: %d,column:%d' %(X_train.shape[0],X_train.shape[1]))