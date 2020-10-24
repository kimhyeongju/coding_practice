# 함수 선언부, 클래스 선언부
def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1,kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

# 전역 변수부
katok = []
select = -1     # 1.추가 2.삽입 3.삭제 4.종료

# 메인 코드부
if __name__ == '__main__':
    while(select != 4):
        select = int(input('선택(1.추가 2.삽입 3.삭제 4.종료) --> '))

        if select == 1:
            data = input('추가할 데이터 --> ')
            add_data(data)
            print(katok)

        elif select == 2:
            pos = int(input('삽입할 위치 --> '))
            data = input('추가할 데이터 --> ')
            insert_data(pos, data)
            print(katok)

        elif select == 3:
            pos = int(input('삭제할 위치 --> '))
            delete_data(pos)
            print(katok)

        elif select ==4:
            exit()

        else:
            print("잘못 입력")
            exit()
