import sys

def coinChange(n) :
    result = 0  # 동전의 개수
    coins = [100,50,10,5,1]

    for coin in coins:
        result += n//coin
        n = n%coin  # 지불하고 남은 액수

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(coinChange(n))

if __name__ == "__main__":
    main()
