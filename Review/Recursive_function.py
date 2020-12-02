def reculsive_function(i):
    if i == 10:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수 호출")
    reculsive_function(i+1)
    print(i, "번째 재귀함수 종료")

reculsive_function(1)