"""
1. Write a Python class BankAccount that manages a simple bank account with the following features: 
Requirements:
•	Initialize with account number, holder name, and initial balance (default 0)
•	Implement deposit(amount) method that adds money (must be positive)
•	Implement withdraw(amount) method that removes money (check sufficient balance)
•	Implement get_balance() method to return current balance
•	Implement transfer(amount, target_account) to transfer money to another account
•	Maintain transaction history (list of all transactions with type, amount, and timestamp)
•	Implement __str__() for readable representation 
"""


from datetime import datetime

class BankAccount:
    def __init__(self,account_number, holder_name,initial_balance = 0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transaction_history = []


    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
            self.transaction_history.append({
                "type": "Deposit",
                "amount": amount,
                "time": datetime.now()
            })
        else:
            print("Invalid deposit amount")


    def withdraw(self, amount):
        if(amount>0 and self.balance>=amount):
            self.balance -= amount
            self.transaction_history.append({
                "type": "Withdraw",
                "amount": amount,
                "time": datetime.now()
            })
        else:
            print("Invalid withdraw amount or insufficient funds")


    def transfer(self, amount, recipient_account):
        if(amount>0 and self.balance>=amount):
            self.balance -= amount
            recipient_account.deposit(amount)
            self.transaction_history.append({
                "type": "Transfer",
                "to": recipient_account.account_number,
                "amount": amount,
                "time": datetime.now()
            })
        else:
            print("Invalid transfer amount or insufficient funds")


    def __str__(self):
        return f"Account Number: {self.account_number}, Holder Name: {self.holder_name}, Balance: {self.balance}"


    def get_transaction_history(self):
        return self.transaction_history


acc1 = BankAccount("1234", "AAA", 1000)
acc2 = BankAccount("5678", "BBB", 500)
acc3 = BankAccount("9876", "CCC")
    
print(acc1)    
acc1.deposit(500)
acc1.withdraw(200)
print(acc1.balance)

acc1.transfer(300, acc2)

print(acc1)
print(acc2)

print(acc3) # defualt balance is 0

print(acc1.get_transaction_history())

acc1.transfer(2000, acc3) # Insufficient funds
acc1.transfer(-100, acc3) # Invalid transfer amount
acc1.transfer(1000, acc3) 

print(acc1)
print(acc3)

print(acc3.get_transaction_history()) 

