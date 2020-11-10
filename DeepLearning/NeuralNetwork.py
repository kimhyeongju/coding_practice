import numpy as np
from functions1 import *

class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes      # 784
        self.hidden_nodes = hidden_nodes    # 100
        self.output_nodes = output_nodes    # 10

        # 2층 hidden layer unit의 w,b 초기화
        self.w2 = np.random.rand(self.input_nodes, self.hidden_nodes)   # w2 = 784 * 100
        self.b2 = np.random.rand(self.hidden_nodes)                     # b2 = 100 * 1

        # 3층 output layer unit의 w,b 초기화
        self.w3 = np.random.rand(self.hidden_nodes, self.output_nodes)  # w3 = 100 * 10
        self.b3 = np.random.rand(self.output_nodes)                     # b3 = 10 * 1

        # learning rate 초기화
        self.learning_rate = 1e-4

    def feed_forward(self):
        delta = 1e-7

        z1 = np.dot(self.input_data, self.w2) + self.b2
        y1 = sigmoid(z1)

        z2 = np.dot(y1, self.w3) + self.b3
        y = sigmoid(z2)

        # cross-entropy
        return -np.sum(self.target_data * np.log(y+delta) + (1-self.target_data) * np.log((1-y)+delta))

    # input_data : 784개, target_data : 10개
    def train(self, training_data):
        self.target_data = np.zeros(self.output_nodes) + 0.01
        self.target_data[int(training_data[0])] = 0.99

        self.input_data = (training_data[1:] / 255.0 * 0.99) + 0.01

        f = lambda x : self.feed_forward()

        self.w2 -= self.learning_rate * numerical_derivative(f,self.w2)
        self.b2 -= self.learning_rate * numerical_derivative(f,self.b2)
        self.w3 -= self.learning_rate * numerical_derivative(f,self.w3)
        self.b3 -= self.learning_rate * numerical_derivative(f,self.b3)

    def predict(self, input_data):
        z1 = np.dot(input_data, self.w2) + self.b2
        y1 = sigmoid(z1)

        z2 = np.dot(y1, self.w3) + self.b3
        y = sigmoid(z2)

        predicted_num = np.argmax(y)
        return predicted_num

