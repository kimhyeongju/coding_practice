"""
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
"""
def solution(n):
    answer = 0
    for x in range(1,n+1):
        if n % x == 0:
            answer += x
    return answer

a = solution(5)
print(a)