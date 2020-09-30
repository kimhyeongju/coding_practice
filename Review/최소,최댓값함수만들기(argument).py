# 최솟값과 최댓값 찾기
def findMin(*x):
    min=1000000
    for i in x:
        if min > i:
            min = i
    return min

print(findMin(1,3,6,4,-1))

def findMax(*x):
    max = 0
    for i in x:
        if max < i:
            max = i
    return max

print(findMax(1,3,6,4,10))