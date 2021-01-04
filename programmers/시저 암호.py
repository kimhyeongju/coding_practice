"""
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다.
문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
"""
def solution(s, n):
    # print(ord("a"), ord("z"), ord("A"), ord("Z"), ord(" "))
    val = []
    for i in s:
        val.append(ord(i))

    answer = ""
    for x in val:
        if x == 32:
            answer = answer + " "
        elif x <= 90 and x+n > 90:
            answer = answer + chr(64 + (x + n)%90)
        elif x >= 97 and x+n > 122:
            answer = answer + chr(96 + (x + n)%122)
        else:
            answer = answer + chr(x + n)

    return answer

a = solution("zy",3)
print(a)
