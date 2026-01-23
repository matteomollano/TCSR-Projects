from BankAccount import BankAccount

# myaccount is an object created from the class BankAccount
# an object is an instance of a class
myaccount = BankAccount(name="Matteo", email="example@gmail.com", bank="Bank A")
# myaccount.display_balance()

myaccount.withdraw(500)
# myaccount.display_balance()

myaccount.deposit(1000)
# myaccount.display_balance()

myaccount.deposit(1000)
myaccount.deposit(500)
myaccount.withdraw(300)
myaccount.withdraw(250)
myaccount.withdraw(130)

# print(myaccount.account_number)
# myaccount.display_transaction_history()

myaccount2 = BankAccount(name="Matteo", email="example2@gmail.com", bank="Bank B")

print(f"Account 1 balance:")
myaccount.display_balance()
print(f"\nAccount 2 balance:")
myaccount2.display_balance()