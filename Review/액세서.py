# getset
class Date:
    def __init__(self, month):
        self.month = month

    def getmonth(self):
        return self.month

    def setmonth(self, month):
        if 1 <= month <= 12:
            self.month = month

today = Date(8)
today.setmonth(15)
print(today.getmonth())

# property
class Score:
    def __init__(self, math):
        self.inner_math = math

    def getscore(self):
        return self.inner_math

    def setscore(self, math):
        if 0 <= math <= 100:
            self.inner_math = math

    math = property(getscore, setscore)

score = Score(90)
score.math = 105    # 허락 안됨
print(score.math)
