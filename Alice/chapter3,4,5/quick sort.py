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

    return array

def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()