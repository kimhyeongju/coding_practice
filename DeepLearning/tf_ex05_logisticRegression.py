import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

loaded_data = np.loadtxt('./diabetes.csv', delimiter=',')

x_data = loaded_data[:, 0:-1]
t_data = loaded_data[:, [-1]]

x = tf.placeholder(tf.float32, [None, 8])
T = tf.placeholder(tf.float32, [None, 1])

w = tf.Variable(tf.random_normal([8,1]))
b = tf.Variable(tf.random_normal([1]))

z = tf.matmul(x,w) + b
y = tf.sigmoid(z)
loss = -tf.reduce_mean(T*tf.log(y) + (1-T)*tf.log(1-y))

learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

predicted = tf.cast(y>0.5, dtype=tf.float32)    # tf.cast: 759개에 대해 return
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, T), dtype=tf.float32))    # tf.equal: 같으면 True 다르면 False를 return

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(20001):
        loss_val, _ = sess.run([loss, train], feed_dict={x: x_data, T: t_data})

        if step % 500 == 0:
            print('step: ', step, ', loss_val: ', loss_val)

    # Accuracy 확인
    y_val, predicted_val, accuracy_val = sess.run([y, predicted, accuracy], feed_dict={x: x_data, T: t_data})

    print('\ny_val.shape: ', y_val.shape, ', predicted_val.shape: ', predicted_val.shape)
    print('\nAccuracy: ', accuracy_val)