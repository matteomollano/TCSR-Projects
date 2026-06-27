import json

expenses = {}
 
def add_expense():
    category = input("Enter a category: ").strip()
    if not category:
        print("Category cannot be empty")
        return
    amount = float(input("Enter amount of $").strip())
    if amount < 0:
        print("Amount must be greater than or equal to 0")
        return

    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)
    print(f"Added ${amount:.2f} to {category}")

def view_expenses():
    # if expenses is empty
    if not expenses:
        print("No expenses recorded yet")
        return
    
    total = 0
    txns = 0
    print("\n--- All Expenses ---")
    
    for category, amounts in expenses.items():
        cat_total = sum(amounts)
        total += cat_total
        txns += len(amounts)
        entries = ", ".join(f"${a:.2f}" for a in amounts)
        print(f"\n {category}: ${cat_total:.2f} ({entries})")
    print(f"\n Categories: {len(expenses)}")
    print(f" Transactions: {txns}")
    print(f" Total Spent: ${total:.2f}\n")
 
def clear_expenses(confirm):
    if confirm:
        expenses.clear()
        print("All expenses cleared")
    else:
        print("Cancelled")
 
def load_from_file():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        print("Expenses loaded from expenses.json")
    except FileNotFoundError:
        print("Error reading the file.")
 
def save_to_file():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("Expenses saved to expenses.json")
 
def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Clear Expenses")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Quit")
        choice = input("Enter your choice (1,2,3,4,5,6): ").strip()
        
        if choice == "1":
            add_expense()
        if choice == "2":
            view_expenses()
        if choice == "3":
            confirm = input("Are you sure? (y/n): ")
            if confirm == "yes" or confirm == "y":
                confirm = True
            else:
                confirm = False
            clear_expenses(confirm)
        if choice == "4":
            save_to_file()
        if choice == "5":
            load_from_file()
        if choice == "6":
            quit()
        
main()