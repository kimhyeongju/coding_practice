"""
입력으로 n개의 수가 주어지면, quick sort를 구현하는 프로그램을 작성하세요.

입력 예시
10 2 3 4 5 6 9 7 8 1

출력 예시
1 2 3 4 5 6 7 8 9 10
"""

def quickSort(array):
    '''
    퀵정렬을 통해 오름차순으로 정렬된 array를반환하는 함수를 작성하세요.
    '''

    if len(array) <= 1:
        return array

    pivot = array[0]

    left = getSmall(array[1:], pivot)
    right = getLarge(array[1:], pivot)

    return quickSort(left) + [pivot] + quickSort(right)


def getSmall(array, pivot):
    data = []

    for a in array:
        if a <= pivot:
            data.append(a)
    return data


def getLarge(array, pivot):
    data = []

    for a in array:
        if a >= pivot:
            data.append(a)
    return data


def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))


if __name__ == "__main__":
    main()
