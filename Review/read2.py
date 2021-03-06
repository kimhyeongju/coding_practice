f = open("test2.txt", "rt", encoding='utf8')

def read1():
    while True:
        text = f.read(1024)
        if len(text) == 0: break
        print(text, end='')
    f.close()

# 행 마다 "숫자 : " 출력
def read2():
    text = ""
    line = 1
    while True:
        row = f.readline()
        if not row: break
        text += str(line) + " : " + row  # 개행문자가 들어있음
        line += 1
    f.close()
    print(text)

def read3():
    rows = f.readlines()

    for row in rows:
        print(row, end='')
    f.close()

def read4():
    rows = f.readlines()  #개행문자를 추가

    for ix, row in enumerate(rows, 1):
        print(f"{ix}:{row}", end='')
    f.close()

read4()