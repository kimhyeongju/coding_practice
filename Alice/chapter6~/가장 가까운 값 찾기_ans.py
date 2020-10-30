import sys


def getNearestInternal(data, m):
    # m과 가장 가까운 값 후보인 두 값을 리턴하는 함수

    if len(data) == 1:
        return (data[0], data[0])
    elif len(data) == 2:
        return (data[0], data[1])

    mid = len(data) // 2

    if data[mid] <= m:
        return getNearestInternal(data[mid:], m)
    else:
        return getNearestInternal(data[:mid + 1], m)


def getNearest(data, m):

    value = getNearestInternal(data, m)  # value[0] : m 이하이면서 가장 가까운 값
                                         # vlaue[1] : m 이상이면서 가장 가까운 값

    if m - value[0] <= value[1] - m:
        return value[0]
    else:
        return value[1]
    return 0


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))


if __name__ == "__main__":
    main()
