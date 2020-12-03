"""
try:
    실행할 명령
except 예외 as 변수:
    오류 처리문
else:
    예외가 발생하지 않을 때의 처리
"""


str = "89점"
try:
    score = int(str)
    print(score)
except: # 모든 예외에 대해
    print("예외가 발생했습니다.")

print("작업완료")
print()


str = "89"
try:
    score = int(str)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자 범위를 벗어났습니다.")

print("작업완료")
print()


try:
    score = int(str)
    a = str[5]
except(ValueError, IndexError):
    print("점수의 형식 또는 첨자 오류")

print("작업완료")
print()


str = "90점"
try:
    score = int(str)
except ValueError as e:
#    e.print()  # Stack Overflow
    print(e)

except IndexError as e:
#    e.print()
    print(e)

print("작업완료")
print()


def test(str):
    score = int(str)
    print(score)

def work1():
    str = "89점"
    try:
        test(str)
    except Exception as e:
        print(e)

work1()

