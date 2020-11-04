def solution(answers):
    arr = [0,0,0]
    temp1 = [2,1,2,3,2,4,2,5,2,1]
    temp2 = [3,3,1,1,2,2,4,4,5,5]
    student1, student2, student3 = [], [], []
    prob_num = len(answers)
    for i in range(prob_num):
        student1.append((i%5)+1)
        student2.append(temp1[i%10])
        student3.append(temp2[i%10])

    for i in range(prob_num):
        if student1[i] == answers[i]:
            arr[0] = arr[0] + 1
        if student2[i] == answers[i]:
            arr[1] = arr[1] + 1
        if student3[i] == answers[i]:
            arr[2] = arr[2] + 1

    result = []

    max_val = max(arr)
    for ix,i in enumerate(arr):
        if i == max_val:
            result.append(ix+1)

    return result

answer = [1,3,2,4,2]

print(solution(answer))
