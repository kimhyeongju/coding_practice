from keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train_data, t_train_data), (x_test_data, t_test_data) = mnist.load_data()


print(x_train_data.shape, t_train_data.shape, x_test_data.shape, t_test_data.shape)

test_img = x_train_data[5]
plt.imshow(test_img)
plt.show()


