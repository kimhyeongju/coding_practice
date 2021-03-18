def main(arr):
    temp = 0
    length = len(arr)

    for i in range(length):
        for j in range(i, length):
            if arr[i] < arr[j]:
                pass
            else:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr

array = [13,1,3,6,11,2,4,12,8,9,5,7,10]

a = main(array)
print(a)
