# n by m 배열 만들기 (잘못된 방법)
n = 3
m = 5
array = [[0]*m]*n
print(array)

array[1][2] = 3
print(array)    # 모든 2인덱스가 3으로 바뀜
print()

# 컴프리헨션을 이용
n = 3
m = 5
array = [[0]*m for _ in range(n)]
print(array)

array[1][2] = 3 # [1][2]인덱스만 3으로 바귐
print(array)
