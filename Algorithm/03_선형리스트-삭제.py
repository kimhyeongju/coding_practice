# 선형리스트 삭제 연산

katok = ['다현', '정연', '모모', '미나', '쯔위', '사나', '지효']

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1,kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

delete_data(5)
print(katok)