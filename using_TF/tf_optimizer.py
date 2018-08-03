import tensorflow as tf

"""optimizer
    =tf.train.GradientDescentOptimizer(learning_rate-0.1)
    train=optimizer.minimize(cost)
"""
X=[1,2,3]
Y=[1,2,3]
"""가중치는 5.0"""
W=tf.Variable(100.0)

hypothesis=X*W
cost=tf.reduce_mean(tf.square(hypothesis-Y))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)
"""
컴퓨터 가중치 얻기
gvs=optimizer.compute_gradients(cost)
가중치 넣기
apply_gradients=optimizer.apply_gradients(gvs)
"""
"""최소 가중치 찾기"""
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10):
    print(step,sess.run(W))
    sess.run(train)