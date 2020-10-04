"""
참가 인원수: user_num
각자 7장씩 패를 갖는 방식
"""

import random

# 패 섞기(shuffle)
def init(user_num):
    deck = list(range(1,49))
    random.shuffle(deck)
    users = [[] for _ in range(user_num)]   # comprehension을 이용하여 이중리스트 생성
    return deck, users

# 패 분배
def assign(users, deck):
    for _ in range(7):
        for user_card in users:
            card = deck.pop(0)
            user_card.append(card)
