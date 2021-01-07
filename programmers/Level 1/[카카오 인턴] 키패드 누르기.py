"""
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

1 2 3
4 5 6
7 8 9
* 0 #

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
hand는 "left" 또는 "right" 입니다.
"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

입출력 예
             numbers	              hand	   result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
"""
def count(target, position):
    count = 0
    v = abs(position - target)
    count += (v // 3) + (v % 3)
    position = target

    return count, position


def solution(numbers, hand):
    answer = ''

    # initial
    left_position = 10
    right_position = 12

    for i in numbers:
        if i == 0:
            i = 11

        if i == 1 or i == 4 or i == 7:
            left_position = i
            answer = answer + "L"

        elif i == 3 or i == 6 or i == 9:
            right_position = i
            answer = answer + "R"

        else:
            l_count, left_change = count(i, left_position)
            r_count, right_change = count(i, right_position)
            if hand == "left":
                if l_count > r_count:
                    right_position = right_change
                    answer = answer + "R"
                else:
                    left_position = left_change
                    answer = answer + "L"

            elif hand == "right":
                if r_count > l_count:
                    left_position = left_change
                    answer = answer + "L"
                else:
                    right_position = right_change
                    answer = answer + "R"


    return answer

a = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
print(a)
