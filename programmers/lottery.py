import random

win_num = [9, 18 , 19, 30, 34, 40]

class Lottery:
    def __init__(self):
        self.rand_num = []
        self.count = 1

    def num_generator(self):
        self.array = random.sample(range(1,46), 6)
        self.array.sort()
        return self.array

    def filter(self,array):
        pass
 
    def run(self, times):
        while True:
            self.rand_num = Lottery.num_generator(self)

            if win_num == self.rand_num:
                print(f"succeed in {self.count}")
                break

            elif self.count >= times:
                break

            else:
                self.count += 1
                if self.count % 1000 == 0:
                    print(f"count: {self.count},  random number: {self.rand_num}")


test = Lottery()
test.run(1000000)


