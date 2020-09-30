# 최솟값과 최댓값 찾기
def findMin(*x):
    min=1000000
    for i in x:
        if min > i:
            min = i
    return min


def findMax(*x):
    max = 0
    for i in x:
        if max < i:
            max = i
    return max

a = list(map(int,input("최솟값: ").split(" ")))
b = list(map(int,input("최댓값: ").split(" ")))

print(findMin(*a))
print(findMax(*b))