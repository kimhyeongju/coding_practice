from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.text import Tokenizer

text = '해보지 않으면 해낼 수 없다'
result = text_to_word_sequence(text)
print(result)

docs = ['먼저 텍스트의 각 단어를 나누어 토큰화힙니다.',
        '텍스트의 단어로 토큰화해야 딥러닝에서 인식됩니다.',
        '토큰화한 결과는 딥러닝에서 사용할 수 있습니다.']

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_counts)    # 단어의 빈도 수
print(token.word_docs)  # 각 단어가 몇 개의 문장에서 나오는지 (순서는 랜덤)
print(token.word_index) # 각 단어의 인덱스
