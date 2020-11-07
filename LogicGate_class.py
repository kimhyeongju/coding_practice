from functions1 import *
import numpy as np

class LogicGate:
    def __init__(self, gate_name, xdata, tdata):
        self.name = gate_name

        # 입력, 정답 데이터 초기화
        self.__xdata = xdata.reshape(4,2)
        self.__tdata = tdata.reshape(4,1)

        # 가중치, bias 초기화
        self.__w = np.random.rand(2,1)
        self.__b = np.random.rand(1)

        # 학습률 learning rate 초기화
        self.__learning_rate = 1e-2

    def __loss_func(self):
        delta = 1e-7

        z = np.dot(self.__xdata, self.__w) + self.__b
        y = sigmoid(z)

        # cross-entropy
        return -np.sum(self.__tdata * np.log(y+delta) + (1-self.__tdata) * np.log((1-y)+delta))


