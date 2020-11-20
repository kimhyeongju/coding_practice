# raise
def calcsum(n):
    if n < 0:
        raise ValueError
    total = 0
    for i in range(n+1):
        total += 1
    return total

try:
    print("sum(1..10) =", calcsum(10))
    print("sum(1..-5) =", calcsum(-5))
except ValueError:
    print("입력값 에러")
print()

# finally
def div_err():
    try:
        print("네트워크 접속")
        a = 2/0
        print("네트워크 통신 수행")
    finally:
        print("접속 해제")

    print("작업 완료")

def comm():
    try:
        print("네트워크 접속")
        d = 0
        if d != 0:
            return
        a = 2/0
        print("네트워크 통신 수행")
    except:
        pass  # 코드블럭은 필요한데 쓸 내용이 없을 때
    finally:  # 예외발생 유무에 관계없이 try 빠져나오면 반드시 수행
        print("접속 해제")
    print("작업 완료")


# assert 조건, 메시지

score = 128
assert score <= 100, "점수는 100 이하여야 합니다."
print(score)
