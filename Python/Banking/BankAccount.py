import random, string
from datetime import datetime

# think of a class as like a recipe
# think of a object as the food you make from the recipe
class BankAccount:
    
    # class constructor
    def __init__(self, name, email, bank):
        self.name = name
        self.email = email
        self.bank = bank
        self.account_number = self.generate_account_number()
    
        self.balance = 250
        self.transaction_history = []
        
    def deposit(self, amount):
        self.balance += amount
        deposit_transaction = {
            "type": "deposit",
            "amount": amount,
            "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "new_balance": self.balance
        }
        self.transaction_history.append(deposit_transaction)
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            withdraw_transaction = {
                "type": "withdraw",
                "amount": amount,
                "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "new_balance": self.balance
            }
            self.transaction_history.append(withdraw_transaction)
        else:
            print(f"You cannot withdraw ${amount}. You only have ${self.balance}")
        
    def display_balance(self):
        print(f"Your balance is ${self.balance}")
        
    def generate_account_number(self):
        num_chars = random.randint(8, 12)
        numbers = string.digits # "0123456789"
        account_number = ""
        for i in range(num_chars):
            account_number += random.choice(numbers)
        return account_number
    
    def display_transaction_history(self):
        print(f"\nTransaction history for the account {self.account_number}:")
        for transaction in self.transaction_history:
            print("\n--------------------------------------------------------------------------------")
            print(f"Date: {transaction["date"]}")
            print(f"A {transaction["type"]} of {transaction["amount"]} was made.")
            
            if transaction['type'] == "deposit":
                print(f"Your balance changed from {transaction["new_balance"] - transaction["amount"]} to {transaction["new_balance"]}")
            else:
                print(f"Your balance changed from {transaction["new_balance"] + transaction["amount"]} to {transaction["new_balance"]}")
                
            print("--------------------------------------------------------------------------------\n")