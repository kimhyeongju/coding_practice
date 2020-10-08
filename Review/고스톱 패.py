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
            user_card.append(card)  # users에 7개의 서로 다른 카드가 할당

# 결과 출력
def print_result(deck,users):
    print("사용자 패")
    for ix, user_cards in enumerate(users,1):
        print(f"{ix}번째 사용자: ", user_cards)
    print(f"남은 패({len(deck)}장)")
    print(deck)

def main():
    user_num = int(input("게임 인원수: "))
    deck, users = init(user_num)
    assign(users, deck)
    print_result(deck, users)

main()
