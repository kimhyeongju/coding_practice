"""
String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
"""
def solution(seoul):
    i = seoul.index("Kim")
    answer = f"김서방은 {i}에 있다"
    return answer

a = solution(["Jane", "Kim"])
print(a)