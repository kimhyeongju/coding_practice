import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 값이 계속 업데이트 되는 변수 node 정의
w1 = tf.Variable(tf.random_normal([1])) # numpy의 random.rand(1)와 비슷함
b1 = tf.Variable(tf.random_normal([1]))

w2 = tf.Variable(tf.random_normal([1,2]))
b2 = tf.Variable(tf.random_normal([1,2]))

# session 생성
sess = tf.Session()

# 변수 node 값 초기화 반드시 해야 함
sess.run(tf.global_variables_initializer())

for step in range(3):
    w1 = w1 - step
    b1 = b1 - step

    w2 = w2 - step
    b2 = b2 - step

    print('step=', step, ', w1=', sess.run(w1), ', b1=', sess.run(b1))
    print('step=', step, ', w2=', sess.run(w2), ', b2=', sess.run(b2),'\n')

sess.close()
