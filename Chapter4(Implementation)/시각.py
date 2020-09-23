"""
정수 N이 입력되면, 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서
3이 하나라도 포함되는 경우의 수를 구하는 프로그램 작성.
    첫째 줄에 정수 N 입력
"""
"""
--- 내가 푼 답 ---

n = int(input())

sec = 0
min = 0
hour = 0
count = 0


for h in range(n+1):
    sec = 0
    min= 0
    hour = h
    for m in range(60):
        sec = 0
        min = m
        for s in range(60):
            sec = s

            temp = str(hour) + str(min) + str(sec)
            for i in temp:
                if i == "3":
                    count += 1
                    break
                # print(temp)
print(count)

            # 아래 처럼 하면 안됨(서로 다른 i 에 대해 두번 카운트 함)
            # for i in range(10):
            #     if sec == (i * 10) + 3 or sec == 30 + i or min == (i * 10) + 3 or min == 30 + i or hour == (i * 10) + 3 or hour == 30 + i:
            #         count += 1
            # print(hour,min,sec,sep=":")
            # print(count)

"""
# 교재 답

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)




