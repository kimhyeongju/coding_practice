import copy

# 깊은 복사
a = [[1,2,3],[4,5,6]]
b = copy.deepcopy(a)  # 깊은 복사

a[0][2] = 6

print(a)
print(b)
