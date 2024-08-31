# Create a class called BankAccount to represent a basic bank account. The class should
# have the following attributes:
# 1. owner: The name of the account owner.
# 2. balance: The current balance of the account.
# Implement the following methods:
# 1. __init__(self, owner, balance): Initializes the BankAccount object with the
# owner's name and initial balance. Ensure that the balance is a non-negative
# integer.
# 2. get_balance(self): Returns the current balance of the account.
# 3. deposit(self, amount): Adds the specified amount to the account balance.
# Ensure that the amount is a positive integer.
# 4. withdraw(self, amount): Subtracts the specified amount from the account
# balance. Ensure that the amount is a positive integer and does not exceed the
# current balance.
# Additionally, use @property and @attribute.setter to encapsulate the balance
# attribute and enforce validation rules.

#miayn balance-n enq property-ii u setteri mej grum 

class BankAccount:
    def __init__(self, owner, balance ):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        print(f"This is your balance {self.__balance}")

    def deposit(self, amount):
        if amount < 0:
            print("The amount must be a positive integer")

        else:
            self.__balance += amount
            print(self.__balance)

    def withdraw(self, amount):
        if amount < 0:
            print("The amount must be a positive integer")

        elif amount > self.__balance:
            print("The amount must not be exceed the current balance.") 

        else:
            self.__balance -= amount
            print(self.__balance)

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        self.new_balance = new_balance

        if new_balance < 0:     
              print("the balance must be a positive integer")

        else:
            self.__balance = new_balance
            print(self.__balance)
    

x = BankAccount("Narek Gabrelyan", 2000)

x.balance = -200




