from tensorflow.keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from keras.layers import Embedding

text = '오랫동안 꿈꾸는 이는 그 꿈을 닮아간다'

token = Tokenizer()
token.fit_on_texts([text])
print(token.word_index)

x = token.texts_to_sequences([text])
print(x)

# 인덱스 수에 하나를 추가해서 원-핫 인코딩 배열 만들기
word_size = len(token.word_index) + 1
x = to_categorical(x, num_classes=word_size)

print()

for ix, words in enumerate(token.word_index.keys()):
    print(f'{words}: {x[0][ix]}')

# 임베딩
model = Sequential()
model.add(Embedding(16, 4))

