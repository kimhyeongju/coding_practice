def solution(answers):
    arr = [0,0,0]
    temp = [2,1,2,3,2,4,2,5,2,1]
    student1, student2, student3 = [], [], []
    prob_num = len(answers)
    for i in range(prob_num):
        student1.append((i%5)+1)
        student2.append(temp[i%10])           # 2,1,2,3,2,4,2,5,2,1

    for i in range(prob_num):
        if student1[i] == answers[i]:
            arr[0] = arr[0] + 1
        if student2[i] == answers[i]:
            arr[1] = arr[1] + 1

    return arr

answer = [1,2,3,4,5,4,2,5,4,5]

print(solution(answer)) # [1]
