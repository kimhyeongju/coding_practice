# 선형리스트 삽입 연산
katok = ['다현', '정연', '쯔위','사나','지효']

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

insert_data(2,'모모')
print(katok)
insert_data(3,'미나')
print(katok)