class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal.")

    def get_balance(self):
        return self.__balance


# Creating object
obj = BankAccount("Faraz", 64894)

print("Account Holder:", obj.name)

obj.withdrawal(5000)
obj.deposit(7800)

print("Current Balance:", obj.get_balance())