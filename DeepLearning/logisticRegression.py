from functions1 import sigmoid
import numpy as np
import pandas_ex01 as pd
import matplotlib.pyplot as plt

data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]

x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-0.1, 1.1)
# plt.show()

a, b = 0, 0
lr = 0.05

for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data*(sigmoid(a * x_data + b) - y_data)
        b_diff = sigmoid(a * x_data + b) - y_data

        a = a - (lr * a_diff)
        b = b - (lr * b_diff)

    if i % 100 == 0:
        print(f'epoch={i}, 기울기={a:.04f}, 절편={b:.04f}')

plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-0.1, 1.1)
x_range = (np.arange(0, 15, 0.1))
plt.plot(x_range, np.array([sigmoid(a * x + b) for x in x_range]))
plt.show()
