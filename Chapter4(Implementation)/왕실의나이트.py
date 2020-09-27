"""
8 X 8 체스판에 나이트가 있다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
행 위치를 1부터 8로, 열 위치를 a부터 h로 표현할 때, 나이트가 이동할 수 있는 경우의 수를 구하는 프로그램 작성
    첫째 줄에 a1과 같이 나이트의 위치한 곳의 좌표를 나타내는 문자열 입력
    경우의 수 출력
"""
"""
--- 내가 풀어 본 것 ---

coor = input()
row = coor[0]
col = int(coor[1])

if row == 'a' or row == 'h':
    if col == 1 or col == 8:
        result = 2
    elif col == 2 or col == 7:
        result = 3
    else:
        result = 4

if row == 'b' or row == 'g':
    if col == 1 or col == 8:
        result = 3
    elif col == 2 or col == 7:
        result = 4
    else:
        result = 6

if row == 'c' or row == 'd' or row == 'e' or row == 'f':
    if col == 1 or col == 8:
        result = 4
    elif col == 2 or col == 7:
        result = 6
    else:
        result = 8

print(result)
"""

# 교재 답

# 나이트의 현재 위치
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하면(값이 0이 아니면) 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)