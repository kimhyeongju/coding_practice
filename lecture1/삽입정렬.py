def main(arr):
    length = len(arr)

    for i in range(length-1):
        j = i
        while arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            if j == 0:
                break
            else:
                j -= 1

    return arr

array = [13,1,3,6,11,2,4,12,8,9,5,7,10]

a = main(array)
print(a)