import numpy as np

# 임의의 기울기와 절편
fake_a_b = [3, 76]
data = [[2, 81], [4, 93], [6, 91], [8, 97]]

x = [i[0] for i in data]  # [2,4,6,8]
y = [i[1] for i in data]  # [81,93,91,97]


def predict(x):
    return fake_a_b[0] * x + fake_a_b[1]


# mse함수
def mse(y_hat, y):
    return ((y_hat - y) ** 2).mean()


# mse함수를 각 y값에 대입하여 최종 값을 구하는 함수
def mse_val(predict_result, y):
    return mse(np.array(predict_result), np.array(y))


predict_result = []  # 예측값이 들어갈 빈 리스트

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print(f"공부한 시간={x[i]}, 실제 점수={y[i]}, 예측 점수={predict(x[i])}")

print("mse 최종값: ", str(mse_val(predict_result, y)))