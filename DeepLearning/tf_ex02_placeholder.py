import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# placeholder node 정의
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = a+b

# session을 만들고 placeholder node를 통해 값을 입력받음
sess = tf.Session()
print(sess.run(c, feed_dict={a:1.0, b:3.0}))
print(sess.run(c, feed_dict={a:[1.0, 2.0], b:[3.0, 4.0]}))

# 연산 추가
d = 100*c
print(sess.run(d, feed_dict={a:1.0, b:3.0}))
print(sess.run(d, feed_dict={a:[1.0, 2.0], b:[3.0, 4.0]}))

sess.close()