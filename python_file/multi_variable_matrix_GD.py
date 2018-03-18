import tensorflow as tf
"""3X5행렬"""
X_data = [
        [73., 80., 75.],
        [93., 88., 93],
        [89., 91., 90.],
        [96., 98., 100.],
        [73., 66., 70.]
        ]
"""5X1행열"""
Y_data = [
        [152.],
        [185.],
        [180.],
        [196.],
        [142.]
        ]
X = tf.placeholder(tf.float32,shape=[None, 3])
Y = tf.placeholder(tf.float32,shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1]),name="weight")
b = tf.Variable(tf.random_normal([1]),name="bias")
"""행렬 곱 연산"""
hypothesis=tf.matmul(X,W)+b

cost=tf.reduce_mean(tf.square(hypothesis-Y))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100000):
    cost_val,hy_val,_=sess.run([cost,hypothesis,train],feed_dict={X:X_data,Y:Y_data})
    if step % 10000 is 0:
        print(step,"COST:",cost_val,"\nPrediction:\n",hy_val)