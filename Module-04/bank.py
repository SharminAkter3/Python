class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000000

    def get_balance(self):
        print(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Oops, You can withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"Owh, You can not withdraw more than {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"Here is your money {amount}")
            print(f"Your balance after withdraw{self.balance}")


SIBL = Bank(12000)
SIBL.withdraw(50)
SIBL.withdraw(2000)
SIBL.withdraw(20000000)
