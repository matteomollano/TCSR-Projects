items = ["apples", "bread", "pasta"]

print("Your Shopping List")
for i in range(len(items)):
    print(str(i+1) + ".", items[i])

while True:
    choice = input("1 to add item, 2 to delete item: ")
    
    # check if they want to add a new item
    if choice == "1":
        new_item = input("Enter a grocery item: ")
        items.append(new_item)
    elif choice == "2":
        index = int(input("Enter item number to delete: "))
        items.pop(index - 1)
    else:
        print("Invalid choice. Enter 1 or 2 only.")
    
    print("Your Shopping List")
    for i in range(len(items)):
        print(str(i+1) + ".", items[i])