from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import tensorflow as tf

np.random.seed(3)
tf.random.set_seed(3)

dataset = np.loadtxt('./pima-indians-diabetes.csv', delimiter=',')
X = dataset[:, 0:8]
Y = dataset[:, 8]

# 구조 결정
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 실행
model.fit(X, Y, epochs=200, batch_size=10)

# 출력
print(f'\n Accuracy:{model.evaluate(X, Y)[1]:.4f}')
