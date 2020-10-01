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


main()
