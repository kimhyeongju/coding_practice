import random

lastest = [9, 10, 15, 29, 33, 37]   # 수정
win_num = [9, 18, 19, 30, 34, 40]


class Lottery:
    def __init__(self):
        return

    def num_generator(self):
        self.array = random.sample(range(1,46), 6)
        self.array.sort()
        return self.array

    def num_generator2(self):
        i = random.randint(0,6)
        r = lastest[i]
        self.array = random.sample(range(1, 46), 6)

        if r in self.array:
            self.array.sort()
            return self.array
        else:
            self.array.pop()
            self.array.append(r)
            self.array.sort()
            return self.array

    def filter(self, array):
        for i in range(4):
            if array[i] + 1 == array[i+1] and array[i+1] + 1 == array[i+2]:
                return True
            else:
                continue
        return False
 
    def run(self, maximum ,times=1):
        temp = []
        count = 1
        for _ in range(times):
            while True:
                rand_nums = Lottery.num_generator(self)

                if Lottery.filter(self, rand_nums) == True:
                    pass
                else:
                    if win_num == rand_nums:
                        print(f"succeed in {count}, number: {rand_nums}")
                        temp.append(count)
                        break

                    elif count >= maximum:
                        print("failed")
                        temp.append("fail")
                        break

                    else:
                        count += 1
                        if count % 50000 == 0:
                            print(f"count: {count},  random number: {rand_nums}")
        print(temp)


test = Lottery()
test.run(10000000,2)

# fail, 3606711, 2960346, fail, 3375173, 976550, fail, 2016942
