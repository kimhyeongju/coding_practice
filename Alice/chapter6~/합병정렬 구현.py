"""
n개의 숫자를 합병정렬을 이용하여 정렬하는 프로그램을 작성하세요.

입력 예시
1 5 6 2 3 8 4 9 7 10
출력 예시
1 2 3 4 5 6 7 8 9 10

문제 조건
입력되는 수의 새구는 최대 100000개입니다.
"""

import sys

def mergeSort(data) :
    '''
    n개의 숫자를 합병정렬을 이용하여 정렬한 결과를 list로 반환하는 함수를 작성하세요.
    '''

    result = []

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(*mergeSort(data))

if __name__ == "__main__":
    main()
