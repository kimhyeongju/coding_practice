"""
정수 N이 입력되면, 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서
3이 하나라도 포함되는 경우의 수를 구하는 프로그램 작성.
    첫째 줄에 정수 N 입력
"""
"""
--- 내가 푼 답 ---
"""


time = [0,0,0]
count = 0


for _ in range(60):
    time[2] += 1
    for i in range(6):
        if time[2] == (i*10) + 3:
            count += 1
    print(time)
    print(count)


