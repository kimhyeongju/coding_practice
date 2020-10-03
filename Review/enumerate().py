"""
enumerate(seq, start=0)
인덱스와 함께 요소를 리턴
seq는 sring,list,tuple,range() 등이 있음
start의 default는 0(값 지정시 해당 값부터 시작)
"""
score = [88,95,70,100,99]

for value in enumerate(score):
    print(value)
print()

for i,value in enumerate(score,1):
    print(f"{i}번째 성적: {value}")
