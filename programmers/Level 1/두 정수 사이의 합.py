"""
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
"""
def solution(a, b):
    answer = 0
    arr = [a,b]
    arr.sort()
    a, b = arr[0], arr[1]
    while b - a != -1:
        answer += a
        a += 1
    return answer

a = solution(3, 3)
print(a)
