class Account:
    accounts = []

    def __init__(self, name, email, address, accountType):
        self.name = name
        self.email = email
        self.address = address
        self.accountNo = name + address
        self.accountType = accountType
        self.__balance = 0
        self.__transactions = []
        self.loan_taken = 0
        self.max_lone = 2
        Account.accounts.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            self.__transactions.append({"type": "Deposite", "amount": amount})
            print(f"\nDeposited ${amount}. Now, new balance is : ${self.__balance }")
        else:
            print("\nInvalid deposit amount !!")

    def withdraw(self, amount):
        if self.__balance <= 0:
            print("\n---the bank is bankrupt.----")
        else:
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                self.__transactions.append({"type": "Withdrawal", "amount": amount})
                print(f"\nWithdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("\n----Withdrawal amount exceeded---")

    def check_balance(self):
        return self.__balance

    def transaction_history(self):
        for transaction in self.__transactions:
            print(f"{transaction['type']}: ${transaction['amount']}")

    def take_lone(self, amount):
        if self.loan_taken < self.max_lone:
            self.__balance += amount
            self.loan_taken += 1
            self.__transactions.append({"type": "Loan", "amount": amount})
            print(f"\nLoan of ${amount} taken. New balance: ${self.__balance}")
        else:
            print("\nLoan taken off.")

    def transfer_amount(self, another_account, amount):
        if another_account in Account.accounts:
            if amount >= 0 and amount <= self.__balance:
                self.__balance -= amount
                another_account.__balance += amount
                self.__transactions.append({"type": "Transfer", "amount": amount})
                print(
                    f"\nTransferred ${amount} to {another_account.name}. Now, balance: ${self.__balance}"
                )
            else:
                print("\nthe bank is bankrupt.")
        else:
            print("\nAccount does not exist.")

    def is_bankrupt(self):
        return True


class User(Account):
    def __init__(self, name, email, address, accountType):
        super().__init__(name, email, address, accountType)


class SavingsAccount(User):
    def __init__(self, name, email, address, interestRate):
        super().__init__(name, email, address, "savings")
        self.interestRate = interestRate

    def apply_interest(self):
        interest = self.__balance * (self.interestRate / 100)
        print("\nInterest is applied !!")
        self.deposit(interest)


class CurrentAccount(User):
    def __init__(self, name, email, address, limit):
        super().__init__(name, email, address, "current")
        self.limit = limit

    def withdraw(self, amount):
        if self._Account__balance <= 0:
            print("\n---the bank is bankrupt.----")
        else:
            if amount > 0 and amount <= self.limit:
                if amount <= self._Account__balance:
                    self._Account__balance -= amount
                    self._Account__transactions.append(
                        {"type": "Withdrawal", "amount": amount}
                    )
                    print(
                        f"\nWithdrew ${amount}. New balance: ${self._Account__balance}"
                    )
                else:
                    print("\nthe bank is bankrupt.")
            else:
                print("\nInvalid withdrawal amount or exceeded limit")


class Admin(Account):
    def __init__(self, name, email, address):
        super().__init__(name, email, address, "admin")

    @staticmethod
    def delete_user(accountNo):
        for user in Account.accounts:
            if user.accountNo == accountNo:
                Account.accounts.remove(user)
                print(f"User {user.name} has been deleted.")
                break
        else:
            print("\n------User not found.-----")

    @staticmethod
    def list_users():
        if len(Account.accounts) != 0:
            for user in Account.accounts:
                if user.name != "admin":
                    print(
                        f"Name: {user.name}, Email: {user.email}, Account No: {user.accountNo}"
                    )
                else:
                    continue
        else:
            print("User not found!!")

    @staticmethod
    def total_available_balance():
        total_balance = 0
        for user in Account.accounts:
            total_balance += user.check_balance()
        print(f"Total Available Balance: ${total_balance}")

    @staticmethod
    def total_loan_amount():
        total_loans = 0
        for user in Account.accounts:
            if "Loan" in [
                transaction["type"] for transaction in user._Account__transactions
            ]:
                total_loans += sum(
                    [
                        transaction["amount"]
                        for transaction in user._Account__transactions
                        if transaction["type"] == "Loan"
                    ]
                )
        print(f"Total Loan Amount: ${total_loans}")

    @staticmethod
    def loan_feature(enable):
        if enable:
            for user in Account.accounts:
                user.max_lone = 2
            print("Loan feature has been enabled.")
        else:
            for user in Account.accounts:
                user.max_lone = 0
            print("Loan feature has been disabled.")


# Main program

currentUser = None
while True:
    if currentUser == None:
        admin_input = input("Are You user/admin/close? ").lower()
        if admin_input == "admin":
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            admin = Admin(name, email, address)
            currentUser = admin

        elif admin_input == "close":
            break

        else:
            choice = input("\n----> Please Register/Login (R/L) : ")
            if choice == "R":
                name = input("Your name to register: ")
                email = input("Your email to register: ")
                address = input("Your addrss to register: ")
                accountType = input(
                    "Savings Account or Special Account (savings/current): "
                )
                if accountType == "savings":
                    interestRate = int(input("Interest rate: "))
                    user = SavingsAccount(name, email, address, interestRate)
                    currentUser = user
                    print("Your account created successfully")
                else:
                    limit = int(input("Overdraft Limit: "))
                    user = CurrentAccount(name, email, address, limit)
                    currentUser = user
                    print("Your account created successfully")
            else:
                name = input("Name :")
                email = input("Email :")

                match = False
                for user in Account.accounts:
                    if user.name == name and user.email == email:
                        currentUser = user
                        changeOfUser = True
                        match = True
                        break
                if match == False:
                    print("\n User Not Found !\n")

    else:
        if currentUser.name == "admin" and currentUser.email == "admin@gmail.com":
            print("\n-----Options------:\n")
            print("1: Create an Account")
            print("2: Delete User")
            print("3: All Users List")
            print("4: Total Available Balance")
            print("5: Total Loan")
            print("6: On/Off Loan Feature")
            print("7: Logout")

            ch = int(input("Choose option: "))
            if ch == 1:
                name = input("Your name to register: ")
                email = input("Your email to register: ")
                address = input("Your addrss to register: ")
                accountType = input(
                    "Savings Account or Special Account (savings/current): "
                )
                if accountType == "savings":
                    interestRate = int(input("Interest rate: "))
                    SavingsAccount(name, email, address, interestRate)
                    print("Your account created successfully")
                else:
                    limit = int(input("Overdraft Limit: "))
                    CurrentAccount(name, email, address, limit)
                    print("Your account created successfully")

            elif ch == 2:
                name = input("Name: ")
                address = input("Address: ")
                accountNo = name + address
                Admin.delete_user(accountNo)

            elif ch == 3:
                Admin.list_users()

            elif ch == 4:
                Admin.total_available_balance()

            elif ch == 5:
                Admin.total_loan_amount()

            elif ch == 6:
                enable = input("Enable or Disable Loan Feature (Y/N): ").lower()
                Admin.loan_feature(enable == "y")

            elif ch == 7:
                currentUser = None
                print("Logged out.")
            else:
                print("Choose Valid Option!!")

        else:
            if currentUser.accountType == "savings":
                print("-----------------------------------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Logout")
                print("-----------------------------------\n")

                op = input("Choose Option: ")

                if op == "1":
                    amount = int(input("Enter deposit amount: "))
                    currentUser.deposit(amount)

                elif op == "2":
                    amount = int(input("Enter withdrawal amount: "))
                    currentUser.withdraw(amount)

                elif op == "3":
                    balance = currentUser.check_balance()
                    print(f"Your current balance is: ${balance}")

                elif op == "4":
                    currentUser.transaction_history()

                elif op == "5":
                    amount = int(input("Enter amount to take loan: "))
                    currentUser.take_lone(amount)

                elif op == "6":
                    receiver_name = input("Enter receiver's name: ")
                    receiver_email = input("Enter receiver's Email: ")
                    amount = int(input("Enter amount to transfer: "))
                    receiver = None
                    for account in Account.accounts:
                        if (
                            account.name == receiver_name
                            and account.email == receiver_email
                        ):
                            receiver = account
                            break
                    if receiver is not None:
                        currentUser.transfer_amount(receiver, amount)
                    else:
                        print("Account does not exist.")

                elif op == "7":
                    currentUser = None

                else:
                    print("Please Choose Valid Option!!")

            else:
                print("-----------------------------------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money")
                print("7. Logout")
                print("-----------------------------------\n")

                op = input("Choose Option: ")

                if op == "1":
                    amount = int(input("Enter deposit amount: "))
                    currentUser.deposit(amount)

                elif op == "2":
                    amount = int(input("Enter withdrawal amount: "))
                    currentUser.withdraw(amount)

                elif op == "3":
                    balance = currentUser.check_balance()
                    print(f"Your current balance is: ${balance}")

                elif op == "4":
                    currentUser.transaction_history()

                elif op == "5":
                    amount = int(input("Enter amount to take loan: "))
                    currentUser.take_lone(amount)

                elif op == "6":
                    receiver_name = input("Enter receiver's name: ")
                    receiver_email = input("Enter receiver's Email: ")
                    amount = int(input("Enter amount to transfer: "))
                    receiver = None
                    for account in Account.accounts:
                        if (
                            account.name == receiver_name
                            and account.email == receiver_email
                        ):
                            receiver = account
                            break
                    if receiver is not None:
                        currentUser.transfer_amount(receiver, amount)
                    else:
                        print("Account does not exist.")

                elif op == "7":
                    currentUser = None

                else:
                    print("Please Choose Valid Option!!")
