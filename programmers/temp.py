
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


    return calender

a = solution(["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"])
print(a)    # [315, 9, 11, 20, 10]
