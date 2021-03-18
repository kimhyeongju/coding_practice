"""
https://programmers.co.kr/learn/courses/30/lessons/17682
"""
def solution(dartResult):
    answer = 0
    score = []
    bonus = []
    option = []
    result = [0,0,0]

    if dartResult[-1] == "S" or dartResult[-1] == "D" or dartResult[-1] == "T":
        dartResult = dartResult + "_"

    dartResult = dartResult.replace('10','X')

    # for i in range(2,9,3):
    #     if dartResult[i] == "*" or dartResult[i] == "#" or dartResult[i] == "_":
    #         pass
    #     else:
    #         dartResult = dartResult.replace(dartResult[i], f"_{dartResult[i]}")

    for i in range(2,6,3):
        if dartResult[i] == "*" or dartResult[i] == "#":
            pass
        else:
            dartResult = dartResult[0:i] + "_" + dartResult[i:]


    for i in range(9):
        if i % 3 == 0:
            if dartResult[i] == 'X':
                score.append(10)
            else:
                score.append(int(dartResult[i]))

        elif i % 3 == 1:
            if dartResult[i] == "S":
                bonus.append(1)
            elif dartResult[i] == "D":
                bonus.append(2)
            elif dartResult[i] == "T":
                bonus.append(3)

        else:
            option.append(dartResult[i])

    for i in range(3):
        result[i] = score[i] ** bonus[i]

        if i >= 1:
            if option[i] == "*":
                result[i-1] *= 2
                result[i] *= 2
            elif option[i] == "#":
                result[i] *= -1
            else:
                pass

        else:
            if option[i] == "*":
                result[i] *= 2
            elif option[i] == "#":
                result[i] *= -1
            else:
                pass

    for ans in result:
        answer += ans

    return answer

a = solution("1S0T1S")
b = solution("2D2S*2S*")
print(a, b, sep=',')

