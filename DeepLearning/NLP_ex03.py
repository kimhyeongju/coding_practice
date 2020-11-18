import numpy as np
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding
import tensorflow as tf

# 영화 리뷰 생성
docs = ['너무 재밌네요', '최고에요', '참 잘 만든 영화에요', '추천하고 싶은 영화입니다', '한 번 더 보고싶네요',
        '글쎄요', '별로에요', '생각보다 지루하네요', '연기가 어색해요', '재미없어요']

# 긍정 리뷰는 1, 부정 리뷰는 0으로 클래스 지정
classes = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)

x = token.texts_to_sequences(docs)
print(x)

padded_x = pad_sequences(x, 4)
print(padded_x)

word_size = len(token.word_index) + 1

model = Sequential()
model.add(Embedding(word_size, 8, input_length=4))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padded_x, classes, epochs=20)

print(f'\n Accuracy: {model.evaluate(padded_x, classes)[1]:.4f}')