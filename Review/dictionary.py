dic = {
    'boy':'소년',
    'school':'학교',
    'book':'책'
}

# .get(,[]) option의 default는 None
print(dic.get('boy'))
print(dic.get('girl'))
print(dic.get('girl','사전에 없는 단어입니다.'),'\n')

# 수정, 추가, 삭제
dic['boy'] = '남자아이' #수정
dic['girl'] = '소녀' #추가
del dic['school'] #삭제

# 키, 값 목록 리턴
print(dic.keys())
print(dic.values())
print(dic.items(),'\n') # 튜플 목록 리턴


keylist = dic.keys()
for key in keylist:
    print(key,dic[key],'\n')

# 사전 업데이트
dic2={
    'student':'학생',
    'teacher':'선생님',
    'book':'서적'
}

dic.update(dic2)    # 덮어쓰기..?
print(dic)