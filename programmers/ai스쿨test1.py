"""
수학 시험을 잘 본 학생은 영어 시험도 잘 봤는지 알아보기 위해 다음과 같이 순위 순서가 일치하는 학생 쌍은 얼마나 되는지 구하려 합니다.

학생들에게 수학 시험 등수를 부여합니다.
학생들에게 영어 시험 등수를 부여합니다.
(A 학생의 수학 시험 등수 < B 학생의 수학 시험 등수) 이면서 (A 학생의 영어 시험 등수 < B 학생의 영어 시험 등수)인 학생 쌍의 수를 셉니다.
학생들의 수학 시험 점수가 담긴 배열 math_scores, 영어 시험 점수가 담긴 배열 english_scores가 매개변수로 주어질 때,
순위 순서가 일치하는 학생 쌍의 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(math_scores, english_scores):
    answer = 0
    num = len(math_scores)
    for i in range(num):
        for j in range(i+1, num):
            if math_scores[i] > math_scores[j] and english_scores[i] > english_scores[j]:
                answer += 1
            elif math_scores[i] < math_scores[j] and english_scores[i] < english_scores[j]:
                answer += 1

    return answer

a = solution([90, 91, 95, 99, 100]	,	[20, 40, 60, 80, 100])
print(a)