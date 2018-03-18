import tensorflow as tf
"""8X4행렬"""
X_data = [
        [1,2, 1, 1],
        [2,1, 3, 2],
        [3, 1, 3,4],
        [4, 1, 5,5],
        [1, 7, 5,5],
        [1, 2, 5,6],
        [1, 6, 6,6],
        [1, 7, 7,7]
        ]
"""8X3행열"""
Y_data = [
        [0,0,1],
        [0,0,1],
        [0,0,1],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [1,0,0],
        [1,0,0]
        ]
X = tf.placeholder(tf.float32,shape=[None, 4])
Y = tf.placeholder(tf.float32,shape=[None, 3])

W = tf.Variable(tf.random_normal([4, 3]),name="weight")
b = tf.Variable(tf.random_normal([3]),name="bias")
"""logit == score"""
score=tf.matmul(X,W)+b
"""softmax"""
hypothesis=tf.nn.softmax(score)

cost=tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis),axis=1))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(optimizer,feed_dict={X:X_data,Y:Y_data})
        if step%200 == 0:
            print(step,sess.run(cost,feed_dict={X:X_data,Y:Y_data}))
    print("-------feed_dict_a")
    a=sess.run(hypothesis,feed_dict={X:[[1,11,7,9]]})
    print(a,sess.run(tf.argmax(a,1)))
    print("-------feed_dict_b")
    b = sess.run(hypothesis, feed_dict={X: [[1, 3, 4, 3]]})
    print(a, sess.run(tf.argmax(b, 1)))
    print("-------feed_dict_all")
    all = sess.run(hypothesis, feed_dict={X: [[1,11, 7, 7],[1, 3, 4, 3],[1, 1, 0, 1]]})
    print(all, sess.run(tf.argmax(all, 1)))