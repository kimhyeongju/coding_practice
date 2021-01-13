"""문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

[abce, abcd, cdx]	2	[abcd, abce, cdx]
abce와 abcd, cdx의 2번째 인덱스 값은 c, c, x입니다.
따라서 정렬 후에는 cdx가 가장 뒤에 위치합니다.
abce와 abcd는 사전순으로 정렬하면 abcd가 우선하므로, 답은 [abcd, abce, cdx] 입니다.
"""
def solution(strings, n):
    temp = []
    answer = []
    for i in strings:
        i = i[n] + i
        temp.append(i)
    temp.sort()

    for i in temp:
        i = i[1:]
        answer.append(i)

    return answer

a = solution(["abce", "abcd", "cdx"], 2)
print(a)