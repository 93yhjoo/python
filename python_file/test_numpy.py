
import tensorflow as tf
import  numpy as np

xy=np.loadtxt('voice.csv',delimiter=',',dtype=np.float64)
x_data=xy[:,0:-1]
y_data=xy[:,[-1]]
X=tf.placeholder(tf.float64,shape=[None,20])
Y=tf.placeholder(tf.float64,shape=[None,1])

W=tf.Variable(tf.cast(tf.random_normal([20,1]),tf.float64),name='weight')
b=tf.Variable(tf.cast(tf.random_normal([1]),tf.float64),name='bias')
hypothesis=tf.sigmoid(tf.matmul(X,W)+b)
cost=-tf.reduce_mean(Y*tf.log(hypothesis)+(1-Y)*tf.log(1-hypothesis))
train=tf.train.GradientDescentOptimizer(learning_rate=0.0000005).minimize(cost)

predicted=tf.cast(hypothesis>0.5,dtype=tf.float64)
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float64))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        cost_val,_=sess.run([cost,train],feed_dict={X:x_data,Y:y_data})
        if step % 20 == 0:


            print(step, cost_val)
    h,c,a=sess.run([hypothesis,predicted,accuracy],feed_dict={X:x_data,Y:y_data})
    print("\nhypo:",h,"\nCorrect(Y):",c,"\nAccuracy:",a)
    sess.close()