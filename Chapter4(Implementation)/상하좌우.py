"""
여행가 A는 N X N 크기의 정사각형 공간에 서 있다. 가장 왼쪽 위 좌표는 (1,1)이며, 오른쪽 아래는 (N,N)이다.
L,R,U,D 명령을 받아서 최종 위치를 출력한다.
N X N 공간을 벗어나면 무시된다.
    첫째 줄에 공간의 크기를 나타내는 N을 입력받음
    둘째 줄에 여행가 A가 이동할 명령을 입력받음
    최종적으로 A의 도착 지점의 좌표(X,Y)가 공백으로 구분하여 출력됨
"""

"""
--- 내가 풀어본 답 ---

n = int(input())
move = list(input().split())
x,y = 1,1

for i in move:
    if i == "L":
        if y == 1:
            y = 1
        else:
            y -= 1

    elif i == "R":
        if y == n:
            y = n
        else:
            y += 1

    elif i == "U":
        if x == 1:
            x = 1
        else:
            x -= 1

    elif i == "D":
        if x == n:
            x = n
        else:
            x += 1
print(x,y, sep=" ")

"""

# 교재 답

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:   # 입력받은 값에 대하여...
            nx = x + dx[i]
            ny = y + dy[i]
    # 범위 벗어날 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx, ny

print(x,y,sep=" ")