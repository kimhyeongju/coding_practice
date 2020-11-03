import sys

def getSlope(a, b):
    return abs((b[1] - a[1]) / (b[0] - a[0]))


def maxSlope(points):
    points.sort()

    result = 0

    for i in range(len(points) - 1):
        result = max(result, getSlope(points[i], points[i + 1]))

    return result


def main():
    n = int(input())
    points = []

    for i in range(n):
        line = [int(x) for x in input().split()]
        points.append((line[0], line[1]))

    print("%.3lf" % maxSlope(points))


if __name__ == "__main__":
    main()
