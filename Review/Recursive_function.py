def reculsive_function(i):
    if i == 10:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수 호출")
    reculsive_function(i+1)
    print(i, "번째 재귀함수 종료")


# factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

f_i = factorial_iterative(5)
f_r = factorial_recursive(5)
print(f_i)
print(f_r)