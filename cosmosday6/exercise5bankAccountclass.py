class Bankaccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("you can have money")
        else:
            self.balance = amount

    def check_balance(self):
        print(self.balance)


acc = Bankaccount()

balance = 2000
acc.deposit(balance)

acc.check_balance()




acc.withdraw(100)

acc.check_balance()