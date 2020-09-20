# shallow copy, deep copy
import copy

a = [1,2,3]
b = a

print("a=",a)
print("b=",b)

a.append(4)

print(a,b,sep=",")
print()
"""
위의 경우 "=" 연산은 얕은 복사를 하는 것을 알 수 있다.
슬라이싱에서도 얕은 복사지만 1차원인 경우와 다차원인 경우 다름. 
"""

# 1차원 리스트
a = [1,2,3]
b = a[:]

a[0] = 0

print(id(a[0]),id(b[0]), sep=",")
print(a,b,sep=",")
print()

# 2차원 리스트
a = [[1,2,3], [4,5,6]]
b = a[:]

a[1][0] = 9   # 2차원의 인덱스에는 얕은 복사... WHY?

print(id(a[0]),id(b[0]), sep=",")
print(a)
print(b)
print()
