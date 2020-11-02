"""
엘리스씨는 1원, 5원, 10원, 50원, 100원 짜리 동전이 무한개(!) 존재하는 가게에 근무한다.
손님이 계산을 하고 난 후, 거스름돈을 돌려주어야 하는데 가능한 적은 수의 동전을 돌려주고 싶다.

예를 들어, 7원을 돌려줘야 한다면 1원을 7개 돌려줄 수도 있지만,
그것보다는 5원 1개와 1원 2개를 돌려주는 것이 적은 수의 동전을 돌려주는 것이므로, 이것이 더 좋은 경우이다.

거스름돈 nn원을 돌려주어야 할 때, 돌려주어야 하는 동전 개수의 최솟값을 출력하는 프로그램을 작성하세요.

입력 예시 1
7
출력 예시 1
3

문제 조건
돌려주어야 하는 거스름돈은 최대 100,000,000입니다.
"""

import sys

def coinChange(n) :
    '''
    n원을 돌려주기 위해 필요한 동전 개수의 최솟값을 반환하는 함수를 작성하세요.
    '''

    return 0

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(coinChange(n))

if __name__ == "__main__":
    main()
