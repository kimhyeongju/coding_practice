"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
"""
# def solution(n):
#     answer = []
#     for i in range(2, n+1):
#         temp = 0
#         while True:
#             for j in range(1,i):
#                 if i % j == 0:
#                     temp += 1
#                 else:
#                     pass
#
#             if temp > 1:
#                 break
#             else:
#                 answer.append(i)
#
#     return answer

import numpy as np
def solution(n):
    arr = []

    for i in range(2, round(np.sqrt(n)) + 1):
        for k in range(i, n//i + 1):
            arr.append(i*k)

    set_arr = set(arr)

    return n - len(set_arr) -1
a = solution(100)
print(a)
