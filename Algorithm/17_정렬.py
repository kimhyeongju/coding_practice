import random
# 함수 선언부
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i

    return minIdx

# 전역 변수부
before = [random.randint(1,99) for _ in range(20)]
after = []


# 메인 코드부
print('정렬 전 --> ', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 --> ', after)