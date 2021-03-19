sorted_arr = []

def merge(arr, m, middle, n):
    i = m
    j = middle + 1
    k = m

    # 작은 순서대로 배열에 삽입
    while i <= middle and j <= n:
        if arr[i] <= arr[j]:
            sorted_arr[k] = arr[i]
            i += 1
        else:
            sorted_arr[k] = a[j]
            j += 1
        k += 1

    # 남은 데이터 삽입
    if i > middle:
        for x in range(n):
            sorted_arr[k] = arr[x]
            k += 1
    else:
        for x in range(middle):
            sorted_arr[k] = arr[x]
            k += 1
    # 정렬된 배열을 삽입
    for x in range(n):
        arr[x] = sorted_arr[x]

def mergeSort(arr, m, n):
    # 크기가 1보다 큰 경우
