# 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교

from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택 정렬
start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print(f"선택 정렬 시간 측정: {end_time - start_time:.5f}초")

# 기본 정렬 라이브러리
start_time = time.time()

array.sort()

end_time = time.time()
print(f"기본 정렬 라이브러리 시간 측정: {end_time - start_time:.5f}초")
