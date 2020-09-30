# 가위바위보 게임
import random
rock=0
scissors=1
paper=2
time=3
win=0
draw=0
for i in range(time):
    me=int(input("0:주먹, 1:가위, 2:보 ->"))
    com=int(random.random()*10)%3 # [random.random() * 원하는 범위 + 시작 숫자]
    print("Computer=",com)
    print(i+1,"번째판 결과:", end='')
    if com == me:
        print("비김")
        draw += 1
    elif com == rock:
        if me == scissors: print("졌음")
        else:
            print("이김")
            win += 1
    elif com == scissors:
        if me == rock:
            print("이김")
            win += 1
        else: print("졌음")
    elif com == paper:
        if me == rock: print("졌음")
        else:
            print("이김")
            win += 1
print("이긴 횟수:",win)
print("진 횟수:",time-win-draw)
print("비긴 횟수:",draw)