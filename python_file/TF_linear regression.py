import tensorflow as tf
import matplotlib.pyplot as plt
X_train=[1,2,3]
Y_train=[1,2,3]
"""W를 임의적인 값으로 바꿔간다."""
W=tf.Variable(tf.random_normal([1]),name="weight")
X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)

"""예상 선형"""
hypothesis=X*W

"""표준 편차의 제곱의 평균"""
cost=tf.reduce_sum(tf.square(hypothesis-Y))

learing_rate=0.1
gradient=tf.reduce_mean((W * X-Y)*X)
descent=W-learing_rate*gradient
update=W.assign(descent)
sess=tf.Session()
"""세션 초기화"""
sess.run(tf.global_variables_initializer())

W_val=[]
cost_val=[]
for step in range(21):
    sess.run(update, feed_dict={X:X_train, Y:Y_train})
    print(step, sess.run(cost,feed_dict={X:X_train,Y:Y_train}),sess.run(W))