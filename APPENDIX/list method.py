a = [2,3,1]

# 마지막에 추가
a.append(4)
print("a.append(4):", a)
print()

# 정렬
a.sort()
print("a.sort():", a)

a.sort(reverse=True)
print("a.sort(reverse=True):", a)
print()

b = sorted(a)
print("result of 'b = sorted(a)':", b)
print("array a:",a)    # a에 영향을 안줌

b = a.sort()
print("result of 'b = a.sort()':", b)  # sort()는 리턴값이 없음
print()

# 특정 인덱스에 추가
a.insert(2,3)
print("2인덱스에 3추가:",a)

# 특정 값 카운트
b = a.count(3)
print("3의 개수:", b)
print()

# 특정 값 삭제
a.remove(2)
print("result of a.remove(2):", a)
print()

"""
remove()와 insert()는 중간의 값을 삭제, 추가한 뒤 리스트 엘리먼트 위치를 다시 조정해야 하므로 O(N)의 시간복잡도를 가진다. 
따라서 시간초과가 발생할 수 있으므로 remove()를 아래와 같은 방법으로 쓰는 것이 좋다. 
"""
a = [1,2,3,4,5]
remove_set = [3,4]  # 삭제할 데이터의 리스트
result = [i for i in a if i not in remove_set]  # 컴프리헨션 이용
print("a:",a)
print(result)
