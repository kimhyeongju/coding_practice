"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
"""
def solution(n, m):
    answer = []
    temp = []
    for common_div in range(1,n+1):
        if n % common_div == 0 and m % common_div == 0:
            temp.append(common_div)
    answer.append(temp[-1])

    temp = []
    if m > n:
        for i in range(1, n+1):
            for j in range(1 , m+1):
                if n*j == m*i:
                    temp.append(n*j)
                    break
    else:
        for i in range(1, m+1):
            for j in range(1 , n+1):
                if m*j == n*i:
                    temp.append(m*j)
                    break
    answer.append(temp[0])

    return answer

a = solution(5, 17)
print(a)