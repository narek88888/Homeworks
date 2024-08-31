# Exercise: Bank Account Hierarchy
# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the
# BankAccount class.
# ● The BankAccount class should have the following attributes and methods:
# ○ Attributes: account_number, balance
# ○ Methods: __init__ (constructor), deposit, withdraw, and get_balance
# ● The SavingsAccount class should inherit from BankAccount and have an
# additional attribute interest_rate. Override the deposit method to add
# interest to the balance when a deposit is made.
# ● The CheckingAccount class should inherit from BankAccount and have an
# additional attribute overdraft_fee. Override the withdraw method to deduct
# the overdraft fee if a withdrawal causes the balance to go below zero.


class BankAccount :
    def __init__(self, account_number, balance) :
        self.account_number = account_number
        self.balance = balance
        

    def deposit(self, amount) :
        self.amount = amount
        if self.amount < 0 :
            print("you cannot deposit a negative number")
        else:
            self.balance += self.amount

    def withdraw(self, amount) :
       self.amount = amount
       if self.amount > self.balance :
           print("the amount must not be more than your balance")
           
       else:
           self.balance -= self.amount
           print(self.balance)    

    def get_balance(self) :
        print(f"This is your balance {self.balance}")

class SavingAccount(BankAccount) :

    def __init__(self, account_number, balance, interest_rate) :
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.amount = amount
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(self.balance)       
                                                        
class CheckingAccount(BankAccount) :

    def __init__(self, account_number, balance, overdraft_fee) :
        super().__init__(account_number, balance)
        self.overdraft_fee = overdraft_fee

    def withdraw(self,amount):
        self.amount = amount

        if self.amount > self.balance:
            self.balance -= self.amount + self.overdraft_fee
        else:
            self.balance -= self.amount
            print(self.balance)    
            
        print(self.balance)    
   
Account3 = CheckingAccount("4444", 1000, 25) 

Account3.withdraw(3000)
