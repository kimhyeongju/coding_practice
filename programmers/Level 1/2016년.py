"""
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다.
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.
"""
import datetime as dt

def solution(a, b):
    answer = ''
    date_2016 = dt.datetime(2016,a,b)
    weekday_2016 = date_2016.weekday()
    if weekday_2016 == 0:
        answer = "MON"
    elif weekday_2016 == 1:
        answer = "TUE"
    elif weekday_2016 == 2:
        answer = "WED"
    elif weekday_2016 == 3:
        answer = "THU"
    elif weekday_2016 == 4:
        answer = "FRI"
    elif weekday_2016 == 5:
        answer = "SAT"
    elif weekday_2016 == 6:
        answer = "SUN"

    return answer
ans = solution(1,1)
print(ans)