print("Welcome to Python Bank!")

balance = 0  # starting balance

def show_menu():
    print("\n--- Main Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")


def check_balance():
    print(f"\nYour current balance is: ${balance}")


def deposit():
    global balance
    amount = input("How much would you like to deposit? $")

    # validate input
    if not amount.isdigit():
        print("Please enter numbers only.")
        return

    amount = int(amount)
    balance += amount
    print(f"Deposited ${amount}. New balance: ${balance}")


def withdraw():
    global balance
    amount = input("How much would you like to withdraw? $")

    # validate input
    if not amount.isdigit():
        print("Please enter numbers only.")
        return

    amount = int(amount)

    if amount > balance:
        print("You cannot withdraw more than your balance!")
    else:
        balance -= amount
        print(f"Withdrew ${amount}. New balance: ${balance}")


# ---- Main Program Loop ----
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using Python Bank! Goodbye!")
        break
    else:
        print("Invalid choice, please pick 1-4.")
