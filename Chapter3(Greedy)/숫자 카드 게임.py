"""
다음 규칙에 따라, 가장 높은 숫자의 카드를 선택해야 한다.
  1. 카드가 N*M형태로 놓여있다.
  2. 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
  3. 그 행에서 가장 낮은 값의 카드를 뽑아야 한다.

첫째 줄에 행과 열의 개수를 공백을 기준으로 입력받음
둘째 줄에 N개 줄에 걸쳐 카드 숫자가 주어짐
"""

"""
--- 혼자 풀어본 것 ---
"""
import sys
from random import randint


N,M = map(int,sys.stdin.readline().split())
cards = []

result_card = 0

for i in range(N):
    cards.append([])
    for _ in range(M):
        cards[i].append(randint(1,100))
print(cards)

for i in range(N-1):
    row_min_cards = min(cards[i])
    if row_min_cards < min(cards[i+1]):
        row_min_cards = min(cards[i+1])

print(row_min_cards)

