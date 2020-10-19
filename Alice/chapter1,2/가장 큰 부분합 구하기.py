"""
정수들의 리스트가 입력으로 들어옵니다. 이 정수들의 리스트를 일부분만 잘라내어 모두 더했을 때의 값을 부분합이라 부릅니다.
이때 가장 큰 부분합을 구해봅시다.

예를 들어, [-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]이 입력으로 들어왔다면
[10, 5, -2, 17]을 모두 더한 30이 정답이 됩니다.
"""
import numpy as np

def maxSubArray(nums):
    arr = []
    for i in range(len(nums)):
        subArray = np.cumsum(nums[i:])
        result = max(subArray)
        arr.append(result)

    return max(arr)

def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

    # test_array = [1,2,3]
    # test = np.cumsum(test_array)
    # print(test)

if __name__ == "__main__":
    main()