# classmethod
class Car:
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()

#clsstr
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"

kim = Human(30,"김태연")
print(kim)