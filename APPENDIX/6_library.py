# min()과 max()
min_value = min(2,4,6,7,10)
max_value = max(2,4,6,7,10)
print(f"min={min_value}, max={max_value}")

# 수식이 문자열일 경우 사용하는 eval()
result = eval("2+3*6")
print(result)

# sort()와 sorted()
import copy

array = [2,6,5,1,7,9,11]
result1 = sorted(array)
result2 = sorted(array, reverse=True)
result3 = copy.deepcopy(array)
array.sort()
result4 = array
print(result1, result2, result3, result4, sep="\n")