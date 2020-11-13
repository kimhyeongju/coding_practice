import tensorflow as tf
import numpy as np

"""
=== tensorflow 1.x version ===

* 연산을 수행하기 위해 다음과 같은 Session을 만들어야 함.
------------------------------------------------
with tf.Session() as sess:
    print(sess.run(c))
------------------------------------------------

* 변수를 초기화 하기 위해서 다음과 같이 초기화 코드를 입력해야 함.
------------------------------------------------
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
------------------------------------------------

* 결과값을 얻기 위해 placeholder에 값을 주고, feed_dict을 통해서 노드에 값 대입함.
------------------------------------------------
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

with tf.Session() as sess:
    print(sess.run(result, feed_dict={a: [1.0], b: [2.0]}))
------------------------------------------------
"""

print(tf.__version__)   # 2.3.1

a = tf.constant(10)
b = tf.constant(20)
c = a + b
d = (a+b).numpy()

print(f'type of c: {type(c)}', f'value_c: {c}', sep='\n')
print(f'type of d: {type(d)}', f'value_d: {d}', sep='\n')

d_numpy_to_tensor = tf.convert_to_tensor(d)
print(type(d_numpy_to_tensor))
print('=============================')

W = tf.Variable(tf.random.normal([1]))
print('initial W =', W.numpy())

for step in range(2):
    W = W + 1.0
    print('step= ', step, ', W =', W.numpy())
print('=============================')

def tensor_sum(x,y):
    return x+y

result = tensor_sum(a,b)

print(type(result))
print(result.numpy())