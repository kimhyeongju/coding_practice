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