def main():
    HANGMAN = """
    ---+
       ㅣ
       0
      /ㅣ\\
       ㅣ
      /  \\
    """
    import random
    rnd = random.randint(1,100)

    n = HANGMAN.splitlines()
    n.pop(0)    # 처음 공백 제거
    # count = 0
    # for i in n:
    #     print(i)
    #     count += 1
    # print(count)

    def hangman(i,lines):
        for line in lines[:i]:
            print(line)

    for i in range(1,7):
        inp = int(input(f"{i}번째 입력: "))
        if inp > rnd:
            print(f"{inp}보다 작음")
            hangman(i,n)
        elif inp < rnd:
            print(f"{inp}보다 큼")
            hangman(i,n)
        else:
            print("정답")
            break

main()
