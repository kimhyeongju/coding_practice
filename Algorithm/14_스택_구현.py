# 함수 선언부
def isStackFull():  # 스택이 찼는지 체크
    global SIZE, stack, top
    if top >= SIZE -1:
        return True
    else:
        return False

def isStackEmpty(): # 스택이 비었는지 체크
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('full')
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택 비었음')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data



# 전역 변수부
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

# 메인 코드부
push('A')
push('B')
push('C')
print(stack)

for _ in range(3):
    data = pop()
    print(data)
print(stack)