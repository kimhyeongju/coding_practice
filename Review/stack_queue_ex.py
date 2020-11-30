# stack
stack = []

stack.append(3)
stack.append(1)
stack.append(4)
stack.append(1)
stack.pop()
stack.append(1)
stack.append(5)
stack.append(9)
stack.pop()

print("-----stack--------")
print(stack)
print(stack[::-1])  # 최상단 원소부터 출력

# queue
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()


print("\n-----queue--------")
print(queue)
queue.reverse()
print(queue)
print(f"list(queue): {list(queue)}")