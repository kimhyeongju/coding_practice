from keras.datasets import mnist
import matplotlib.pyplot as plt
import sys

(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()
print(f"학습셋 이미지 수: {X_train.shape[0]}개")
print(f"테스트셋 이미지 수: {X_test.shape[0]}개")

plt.imshow(X_train[0], cmap='Greys')
plt.show()

for x in X_train[0]:
    for i in x:
        sys.stdout.write(f"{i}\t")
    sys.stdout.write("\n")

