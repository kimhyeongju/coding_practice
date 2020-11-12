import sys

def fKnapsack(materials, m) :
    # 물건을 가성비 순서대로 넣기
    # x[0]:무게, x[1]:가치

    materials = sorted(materials, key = lambda x : x[1]/x[0], reverse=True)

    weight = 0
    value = 0

    for i in range(len(materials)):
        """
        1. 물건을 넣어도 버틸만한 무게일 때
        2. 물건을 넣으면 딱 m만큼 무게가 될 때
        3. 물건을 다 넣으면 무게가 m을 넘어갈 때
        """

        if weight + materials[i][0] < m:
            weight += materials[i][0]
            value += materials[i][1]

        elif weight + materials[i][0] == m:
            weight += materials[i][0]
            value += materials[i][1]
            return value

        else:
            temp = m - weight   # 배낭에 남은 공간
            value += temp * (materials[i][1]/materials[i][0])
            return value

    return value

def main():
    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    materials = []

    for i in range(n) :
        data = [int(x) for x in input().split()]
        materials.append( (data[0], data[1]) )

    print("%.3lf" % fKnapsack(materials, m))

if __name__ == "__main__":
    main()
