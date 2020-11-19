from keras.datasets import mnist
import matplotlib.pyplot as plt
import sys, os
from keras.utils import np_utils

(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()
print(f"학습셋 이미지 수: {X_train.shape[0]}개")
print(f"테스트셋 이미지 수: {X_test.shape[0]}개")

plt.imshow(X_train[13], cmap='Greys')
plt.show()

for x in X_train[13]:
    for i in x:
        sys.stdout.write(f"{i}\t")
    sys.stdout.write("\n")

X_train = X_train.reshape(X_train.shape[0], 784)    # reshape(총 샘플 수, 1차원 속성의 수)

# keras에 최적화하기 위해, 값을 0과 1사이로 변환.
X_train = X_train.astype('float64')     # 나누기 전 실수형으로 변환
X_train = X_train / 255

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255

print(f"class: {Y_class_train[13]}")

# one-hot encoding
Y_train = np_utils.to_categorical(Y_class_train, 10)
Y_test = np_utils.to_categorical(Y_class_test, 10)

print(Y_train[13])
