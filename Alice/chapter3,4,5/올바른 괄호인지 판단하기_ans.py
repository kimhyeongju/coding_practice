"""
본 문제에서는 입력으로 주어지는 괄호가 올바른 괄호인지를 판단하는 프로그램을 작성합니다.

예를 들어, ‘(())’ 은 올바른 괄호이지만, ‘(()))’, 혹은 ‘(()()(‘ 는 올바른 괄호가 아닙니다.

올바른 괄호일때 ‘YES’를, 올바르지 않은 괄호일때 ‘NO’를 출력해 봅시다.

입력 예시 1
(())()
출력 예시 1
YES

입력 예시 2
(())())()
출력 예시 2
NO
"""

def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''
    # 기저조건 처리
    if len(p) == 0:
        return "YES"
    elif len(p) == 1:
        return "NO"

    # p에서 인접한 괄호쌍을 찾아 제거
    for i in range(len(p) - 1):
        if p[i] == '(' and p[i + 1] == ')':
            q = p[:i] + p[i + 2:]
            return checkParen(q)  # checkParen()함수 다시 호출

    return "NO"


def main():
    '''
    Do not change this code
    '''

    x = input()
    print(checkParen(x))


if __name__ == "__main__":
    main()


