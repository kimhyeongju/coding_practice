"""
XX쇼핑센터는 다음과 같이 회원 등급제를 운영하고 있습니다.

등급	기준
브론즈	최근 30일간 0원 이상 10,000원 미만 구매 고객
실버	최근 30일간 10,000원 이상 20,000원 미만 구매 고객
골드	최근 30일간 20,000원 이상 50,000원 미만 구매 고객
플래티넘	최근 30일간 50,000원 이상 100,000원 미만 구매 고객
다이아몬드	최근 30일간 100,000원 이상 구매 고객
등급은 브론즈 → 실버 → 골드 → 플래티넘 → 다이아몬드 순으로 높아집니다.

고객의 2019년 1월 1일 ~ 2019년 12월 31일 기간 동안 구매 기록이 문자열 형태로 담긴 배열 purchase가 매개변수로 주어질 때,
각 등급별 유지 기간을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
purchase의 길이는 1 이상 365 이하입니다.
purchase의 원소는 "2019/MM/DD X" 형식입니다.
2019/MM/DD는 2019년 MM월 DD일을 의미하며, "2019/01/01"에서 "2019/12/31"사이입니다.
구매 기록은 날짜 순으로 정렬되어 있습니다.
같은 날짜의 구매 기록이 중복해서 주어지지 않습니다.
'X'는 구매 금액을 나타내며 1,000 이상 200,000 이하인 자연수입니다.
구매 금액은 1,000원 단위로만 주어집니다.
정답 배열은 [브론즈 기간, 실버 기간, 골드 기간, 플래티넘 기간, 다이아몬드 기간] 순서로 채워서 return 해주세요.
"""

import datetime
def solution(purchase):
    answer = [0] * 5
    init = datetime.date(2019, 1, 1)
    arr_date = []
    calender = [0] * 365

    num = len(purchase)

    for i in range(num):
        year = int(purchase[i][:4])
        month = int(purchase[i][5:7])
        day = int(purchase[i][8:10])
        arr_date.append(datetime.date(year, month, day))

    for i in range(num):
        start = (arr_date[i] - init).days
        if start <= 335:
            for j in range(30):
                calender[start + j] += int(purchase[i][11:])
        else:
            calender[335:] += int(purchase[i][11:])

    for i in calender:
        if i < 10000:
            answer[0] += 1

        elif i >= 10000 and i < 20000:
            answer[1] += 1

        elif i >= 20000 and i < 50000:
            answer[2] += 1

        elif i >= 50000 and i < 100000:
            answer[3] += 1

        else:
            answer[4] += 1


    return answer

a = solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"])
print(a)    # [315, 9, 11, 20, 10]
