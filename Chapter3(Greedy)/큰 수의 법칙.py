"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만든다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
N=배열의 크기
M=숫자가 더해지는 횟수
[2,4,5,4,6]이 있을 때 M=8이고 K=3이면 결과는,
6+6+6+5+6+6+6+5 = 46이다.
""""

"""
--- 혼자 풀어본 것 ---

from random import randint

array = []
N = randint(2,1000)
M = randint(1,10000)
K = randint(1,M)

# array = [2,4,5,4,6]
# N = 5
# M = 8
# K = 3
sum = 0

for _ in range(N):
  array.append(randint(1,10000))


array.sort(reverse=True)

first_value = array[0]
second_value = array[1]

a = M // (K+1)
b = M % (K+1)

for _ in range(a):
  sum += (first_value * K) + second_value
sum += first_value * b

print(N,M,K, sep=" ")
print(sum)

"""

# N,M,K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력받은 수들 정렬하기
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

  print(result)

"""

내가 풀은 것이 효율적인 답안 예시로 나왔음!
while문 이용하는 방법도 알아두기

"""