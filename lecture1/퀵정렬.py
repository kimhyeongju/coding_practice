def quickSort(arr, start, end):

    if start >= end:    # 원소가 1개인 경우 그대로 두기
        return

    pivot = start
    left_idx = start + 1
    right_idx = end

    while left_idx <= right_idx:    # 엇갈릴 때까지 반복

        while left_idx <= end and arr[left_idx] <= arr[pivot]:  # 피벗 값보다 큰 값을 만날 때까지
            left_idx += 1

        while right_idx > start and arr[right_idx] >= arr[pivot]:   # 피벗 값보다 작은 값을 만날 때까지
            right_idx -= 1

        if left_idx > right_idx:    # 엇갈린 상태면 피벗 값과 교체
            temp = arr[right_idx]
            arr[right_idx] = arr[pivot]
            arr[pivot] = temp

        else:
            temp = arr[left_idx]
            arr[left_idx] = arr[right_idx]
            arr[right_idx] = temp

    quickSort(arr, start, right_idx - 1)
    quickSort(arr, right_idx + 1, end)


def main(arr):
    number = len(arr)
    quickSort(arr, 0, number - 1)

    return arr


array = [3, 4, 6, 8, 9, 1, 2, 5, 7]
"""
3, 4, 6, 8, 9, 1, 2, 5, 7
3, 1, 6, 8, 9, 4, 2, 5, 7
3, 1, 2, 8, 9, 4, 6, 5, 7
2, 1, 3, 8, 9, 4, 6, 5, 7   right_idx:2, left_idx:3
2, 1
1, 2
       , 8, 9, 4, 6, 5, 7
       , 8, 7, 4, 6, 5, 9
       , 5, 7, 4, 6, 8, 9   right_idx:7, left_idx:8
       , 5, 7, 4, 6
       , 5, 4, 7, 6
       , 4, 5, 7, 6
             , 7, 6
             , 6, 7
"""
a = main(array)
print(a)
