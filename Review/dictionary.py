# 사전 관리
dic = {
    'boy':'소년',
    'school':'학교',
    'book':'책'
}
print(dic.get('girl')) # .get(,[]) option의 default는 None
print(dic.get('girl','사전에 없는 단어입니다.'),'\n')