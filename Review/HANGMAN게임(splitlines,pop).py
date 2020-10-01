def main():
    HANGMAN = """
    ---+
       ㅣ
       0
      /ㅣ\\
      /  \\
    """
    import random
    rnd = random.randint(1,100)

    n = HANGMAN.splitlines()
    # n.pop(0)
    print(n)

main()
