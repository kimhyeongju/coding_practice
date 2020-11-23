try:
    f = open("test1.txt", "rt", encoding='utf8')
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()