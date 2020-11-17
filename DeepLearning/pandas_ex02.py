from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv('./iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
print(df.head())

sns.pairplot(df, hue='species')
plt.show()

dataset = df.values
X = dataset[:, 0:4].astype(float)
Y_obj = dataset[:, 4]

# 문자열인 Y값을 숫자로 바꿔주는 작업
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)  # 문자열 array가 array([1,2,3])으로 바뀜

# 활성화 함수를 적용하기 위해 Y값을 0과 1로 변환
Y_encoded = tf.keras.utils.to_categorical(Y)    # array([1,2,3])이 array([1., 0., 0.,], [0., 1., 0.], [0., 0., 1.])으로 바뀜
model = Sequential()
model.add(Dense(16, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))   # 출력값이 3개

# 컴파일
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 실행
model.fit(X, Y_encoded, epochs=50, batch_size=1)

print(f'\n Accuracy:{model.evaluate(X, Y_encoded)[1]:.4f}')


