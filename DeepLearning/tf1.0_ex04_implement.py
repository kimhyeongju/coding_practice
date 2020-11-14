import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

loaded_data = np.loadtxt('./data-01.csv', delimiter=',')

x_data = loaded_data[:,0:-1]
y_data = loaded_data[:,[-1]]

print("x_data shape: ", x_data.shape)
print("y_data shape: ", y_data.shape)

w = tf.Variable(tf.random_normal([3,1]))
b = tf.Variable(tf.random_normal([1]))

x = tf.placeholder(tf.float32, [None, 3])
T = tf.placeholder(tf.float32, [None, 1])

y = tf.matmul(x,w) + b  # 현재 x,w,b로 계산된 값
loss = tf.reduce_mean(tf.square(y-T))   # MSE 손실함수

learning_rate = 1e-5
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())     # variable node 초기화
    for step in range(8001):
        loss_val, y_val, _ = sess.run([loss, y, train], feed_dict={x: x_data, T: y_data})

        if step % 400 == 0:
            print('step: ', step, ', loss_val: ', loss_val)
    print('\nPrediction is ', sess.run(y, feed_dict={x: [[100,98,81]] }))