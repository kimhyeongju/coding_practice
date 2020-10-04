import random

# 패 섞기(shuffle)
def init(user_num):
    deck = list(range(1,49))
    random.shuffle(deck)
    users = [[] for _ in range(user_num)]   # comprehension을 이용하여 이중리스트 생성
    return deck, users
