# property2
class Date:
    def __init__(self, month):
        self.inner_month = month

    @property
    def month(self):
        return self.inner_month

    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.inner_month = month

today = Date(8)
today.month = 15
print(today.month)

# hidden
class Score:
    def __init__(self, math):
        self.__math = math

    def getscore(self):
        return self.__math

    def setscore(self, math):
        if 0 <= math <= 100:
            self.__math = math

    math = property(getscore, setscore)
