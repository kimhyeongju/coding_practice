"""
다음 규칙에 따라, 가장 높은 숫자의 카드를 선택해야 한다.
  1. 카드가 N*M형태로 놓여있다.
  2. 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
  3. 그 행에서 가장 낮은 값의 카드를 뽑아야 한다.

첫째 줄에 행과 열의 개수를 공백을 기준으로 입력받음
둘째 줄에 N개 줄에 걸쳐 카드 숫자가 주어짐
"""

"""
--- 내가 풀어본 것 ---

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

"""

import sys
n, m = map(int,sys.stdin.readline().split())
result = 0

# min() 함수를 이용하는 답안
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 2중 반복문 구조를 이용하는 답안
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)