# 손님에게 거슬러 주어야 할 금액이 N원일때 500원, 100원, 50원, 10원의 최소 개수


N = int(input("금액을 입력하세요: "))
coin_types = [500,100,50,10]
count = 0

for coin in coin_types:
  count += N // coin
  N = N % coin
print(f"최소 동전 개수: {count}개")
