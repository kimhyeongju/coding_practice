stack = [None,None,None,None,None]
top = -1

# push
top += 1
stack[top] = 'A'
top += 1
stack[top] = 'B'
top += 1
stack[top] = 'C'

print(stack)

# pop
data = stack[top]
print(data)
stack[top] = None
top -= 1
print(stack)
