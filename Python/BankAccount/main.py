# global variable
balance = 0

def menu():
    print("--- Main Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

# parameter: input to a function
# balance here is a local variable
def check_balance():
    global balance
    print(f"Your balance is ${balance}")
    
def deposit_money():
    global balance
    amount = input("How much would you like to deposit? $")
    
    while amount.isdigit() == False or amount == "0": # not a real number
        print("Enter a positive number")
        amount = input("How much would you like to deposit? $")
    
    amount = int(amount)
    # balance = balance + amount
    balance += amount

def withdraw_money():
    global balance
    amount = input("How much would you like to withdraw? $")
    
    while amount.isdigit() == False or amount == "0": # not a real number
        print("Enter a positive number")
        amount = input("How much would you like to withdraw? $")
    
    amount = int(amount)
    
    if amount > balance:
        print("You cannot withdraw more than your balance.")
    else: # amount <= balance
        balance -= amount
    
    
if __name__ == "__main__":
    print("Welcome to Python Bank!")
    while True:
        menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            break
        else:
            print("Invalid option. Choose 1-4 only.")