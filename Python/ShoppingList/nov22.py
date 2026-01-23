# import questionary

items = ["apples", "pasta", "lettuce"]
items.append("bread")

items.pop(0)

while True:
    for i in range(len(items)):
        print(str(i+1) + ". " + items[i])

    choice = input("1 to add item, 2 to delete item, 3 to exit: ").strip()

    if choice == "1":
        new_item = input("Enter item: ")
        items.append(new_item)
    elif choice == "2":
        while True:
            try: # hw: use a while loop to get new input here
                index = int(input("Enter item number to delete: ")) - 1
                items.pop(index)
                break
            except IndexError as ie:
                print("Item", index+1, "doesn't exist")
                print("Enter between 1 and", len(items))
            except ValueError as ve:
                print("Enter item number, not name.")
    elif choice == "3":
        # hw: add a checkbox here using questionary library
        # result = questionary.checkbox(
        #     message="Select groceries:",
        #     choices=items
        # ).ask()
        selection = input("Are you satisfied with your order? (Yes/No): ").lower()
        if selection == "yes":
            print("Thank you for shopping with us!")
            break
        else:
            anything_else = input("Would you like to add or delete anything else? (Yes/No): ").lower()
            if anything_else != "yes":
                break 
    else:
        print("Invalid. Please enter 1, 2, or 3 only.")