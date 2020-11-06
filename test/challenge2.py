def solution(a):
    arr = []
    for x in range(len(a)-1):

        temp = [a[x],a[x+1]]
        k = 1
        count = 2

        for i in range(x+1,len(a)-2):
            if i + k + 1 == len(a)-1 or i + k + 1 == len(a)-2:
                if a[i+k] in temp or a[i+k+1] in temp:
                    count += 2
                    break
            else:
                if a[i+k] in temp or a[i+k+1] in temp:
                    k = k+1
                    count += 2
                    # print(a[i+1],a[i+2])
                else:
                    pass
        arr.append(count)

        return arr


a = [5,0,5,2,5,2]

print(solution(a))
