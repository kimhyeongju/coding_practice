import tensorflow.compat.v1 as tf   # 새로운 버전에서는 session이 없다..?
tf.disable_v2_behavior()

# 상수 노드 정의
a = tf.constant(1.0, name='a')
b = tf.constant(2.0, name='b')
c = tf.constant([[1.0,2.0],[3.0, 4.0]])

# print(a)
# print(a+b)
# print(c)

# session을 만들고 node간의 tensor연산 실행
sess = tf.Session()
print(sess.run([a,b]))
print(sess.run(c))
print(sess.run(a+b))

sess.close()