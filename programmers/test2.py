def solution(numbers):
    arr = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            val = numbers[i] + numbers[j]
            arr.append(val)

    arr.sort()
    n = 0
    while n < len(arr) - 1:
        if arr[n] == arr[n+1]:
            arr.pop(n)
        else:
            n += 1


    answer = []
    print(arr)


numbers = [2,1,3,4,1]   # result = [2,3,4,5,6,7]

solution(numbers)