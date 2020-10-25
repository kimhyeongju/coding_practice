# 함수 선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE-1:
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return  data

# 전역 변수부
SIZE = 3
queue = [ None for _ in range(SIZE)]
front = rear = -1   # 빈 상태 (두 값이 같으면 빈 큐)

# 메인 코드부
enQueue('A')
enQueue('B')
print(queue)

data = deQueue()
print(data)
print(queue)

enQueue('C')
print(data)
print(queue)

data = deQueue()
print(data)
print(queue)