# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance.
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balance
# of $1000.
# We deposit $500 and withdraw $200 from the account and print the account
# information.


class BankAccount :
    def __init__(self, account_holder, balance) :
      self.account_holder = account_holder
      self.balance = balance
     
    def deposit(self, amount):
      
      if amount < 0:
         print("You cannot deposit negative number")
      else:
         self.balance += amount
         print(self.balance)

    def withdraw(self, amount) :
      if amount > self.balance :
          print("the amount must not be more than your balance")
      else:
          self.balance -= amount
          print(self.balance)
             
    def get_balance(self):
        print(f"this is your balance {self.balance}")

    
bank_account_1 = BankAccount("Narek Gabrelyan", 1000)

bank_account_1.withdraw(500)
bank_account_1.get_balance()
