from functions1 import *
import numpy as np

class LogicGate:
    def __init__(self, gate_name, xdata, tdata):
        self.name = gate_name

        # __(variable): private로 선언 -> 외부에서 못 바꿈
        # 입력, 정답 데이터 초기화
        self.__xdata = xdata.reshape(4,2)   # 입력데이터: (0,0),(0,1),(1,0),(1,1);
        self.__tdata = tdata.reshape(4,1)

        # 가중치, bias 초기화
        self.__w = np.random.rand(2,1)
        self.__b = np.random.rand(1)

        # 학습률 learning rate 초기화
        self.__learning_rate = 1e-2

    # 손실함수
    def __loss_func(self):
        delta = 1e-7

        z = np.dot(self.__xdata, self.__w) + self.__b
        y = sigmoid(z)

        # cross-entropy
        return -np.sum(self.__tdata * np.log(y+delta) + (1-self.__tdata) * np.log((1-y)+delta))

    # 손실 값 계산
    def error_val(self):
        delta = 1e-7

        z = np.dot(self.__xdata, self.__w) + self.__b
        y = sigmoid(z)

        # cross-entropy
        return -np.sum(self.__tdata * np.log(y+delta) + (1-self.__tdata)*np.log((1-y)+delta))

    # 수치미분을 이용하여 손실함수가 최소가 될 때까지 학습
    def train(self):
        f = lambda x : self.__loss_func()

        print("Initial erro value = ", self.error_val())

        for step in range(8001):
            self.__w -= self.__learning_rate * numerical_derivative(f, self.__w)
            self.__b -= self.__learning_rate * numerical_derivative(f, self.__b)

            if step % 400 == 0:
                print("step = ", step, "error value = ", self.error_val())

    # 미래 값 예측 함수
    def predict(self, input_data):
        z = np.dot(input_data, self.__w) + self.__b
        y = sigmoid(z)

        if y > 0.5:
            result = 1
        else:
            result = 0

        return y, result