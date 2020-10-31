import sys
import math

def mergeSort(data) :
    if len(data) == 1:
        return data

    mid = len(data)//2

    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    result = []

    leftPtr = 0
    rightPtr = 0

    while leftPtr < len(left) or rightPtr < len(right):
        leftValue = left[leftPtr] if leftPtr < len(left) else math.inf
        rightValue = right[rightPtr] if rightPtr < len(right) else math.inf

        if leftValue < rightValue:
            result.append(leftValue)
            leftPtr += 1
        else:
            result.append(rightValue)
            rightPtr += 1

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()
