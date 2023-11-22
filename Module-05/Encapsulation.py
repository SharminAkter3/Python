# encapsulation --> hide details
# access modifier --> public, private, protected
class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name  # public
        self._branch = "patiya"  # protected
        self.__balance = initial_deposit  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount

        else:
            return f"you have no money"


rafsan = Bank("Rafsan Haq", 10000)

print(rafsan.holder_name)
# rafsan.balance = 0
# print(rafsan.__balance)
rafsan.holder_name = "rahaman"
rafsan.deposit(40000)
print(rafsan.get_balance())
print(rafsan.holder_name)
# print(rafsan._branch)
print(dir(rafsan))
# print(rafsan.Bank__get_balace())
