def quickSort(arr, start, end):
    pivot = 0
    left_idx = 0
    right_idx = 0
    temp = 0

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


array = [10, 3, 4, 6, 8, 9, 1, 2, 5, 7]
a = main(array)
print(a)
