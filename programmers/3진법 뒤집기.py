"""
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
답을 도출하는 과정은 다음과 같습니다.
n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
45	        1200	        0021	        7
따라서 7을 return 해야 합니다.
"""

def solution(n):
    ternary = []

    while True:
        r = n % 3
        q = n // 3
        ternary.append(r)
        if q == 0:
            break
        elif q <= 2:
            ternary.append(q)
            break
        else:
            n = q


    answer = 0
    s = len(ternary)
    for i in ternary:
        s -= 1
        answer += i * (3 ** s)

    return answer

a = solution(45)
print(a)