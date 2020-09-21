"""
어떠한 수 N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행한다.
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
    1. N에서 1을 뺀다.
    2. N을 K로 나눈다.
첫쨰 줄에 N과 K(=<N)가 공백으로 구분
둘쨰 줄에 수행의 최솟값을 출력
"""

"""
--- 스스로 풀어 본 것 ---

import time
import sys

start_ = time.time()
N , K = map(int, sys.stdin.readline().split())
count = 0

while N > 1:
    if N % K == 0:
        N = N // K
        count = count + 1

    else:
        N = N - 1
        count = count + 1
end_ = time.time()
print(end_ - start_)    # 걸린시간: 4.25 @(100000,9)

print(count)

"""

import time
start_ = time.time()

n ,k = map(int, input().split())
result = 0

# N이 k 이상이라면 K로 계속 나누기
while n>=k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

end_ = time.time()
print(end_ - start_)  # 걸린시간: 10.64 @(100000,9)

print(result)

# --- 내가 푼 게 실행시간이 더 적게 걸림 ---


