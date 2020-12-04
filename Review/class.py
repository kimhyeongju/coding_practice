class Account:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def deposit(self, money):
        self.balance += money

    def inquire(self):
        print(f"{self.name}의 잔액:{self.balance}")


class Asset(Account):
    def __init__(self, balance, name, debt, stock):
        super().__init__(balance, name)
        self.debt = debt
        self.stock = stock

    def inquire(self):
        print(f"{self.name}의 자산:{self.balance + self.stock - self.debt}")

A_john = Asset(5000, "john", 1000, 0)
A_john.deposit(10000)
A_john.inquire()

