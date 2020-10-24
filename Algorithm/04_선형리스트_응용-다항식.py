# 함수 선언부
def printPoly(p_x):
    term = len(p_x) -1  # 최고항 숫자 = 배열길이 - 1
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        coef = p_x[i]   # 계수
        if coef >= 0:
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + ''
        term -= 1

    return  polyStr


# 전역 변수부
px = [4,-3,8,2]  # 4x^3 + 3x^2 + 8x^1 + 2x^0

# 메인 코드부

pStr = printPoly(px)
print(pStr)