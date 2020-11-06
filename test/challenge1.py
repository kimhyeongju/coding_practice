

def solution(s):
    count1 = 0
    count2 = 0

    while True:

        s = list(s)
        temp = []

        for i in s:
            if i == '0':
                temp.append(s.index(i))
                count1 += 1

        for i in temp:
            s.pop(i)

        num = len(s)

        a = []
        result = ""
        q,r = 0, 0
        binary_digit = 0
        while True:
            q = int(num/2)
            r = int(num%2)
            binary_digit += 1
            a.append((q,r))
            if q != 0:
                num = q
            else:
                count2 += 1
                break
        for i in range(len(a)):
            result += str(a[-(i+1)][1])
        print(result)

        s = result

        if s == "1":
            return count2, count1
            break



s = "110010101001"
print(solution(s))