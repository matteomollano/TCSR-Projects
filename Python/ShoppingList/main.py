items = ["apples", "bread", "ramen"]

print("Your Shopping List")
for i in range(len(items)):
    print(str(i+1) + ".", items[i])

# 1. apples
# 2. bread
# 3. ramen
# 4. peanut butter

while True:
    choice = input("1 for new item, 2 for delete item: ")
    
    if choice == "1":
        x = input("Enter a grocery item: ")
        items.append(x)
    elif choice == "2":
        x = int(input("Enter item number to delete: "))
        items.pop(x-1)
    else:
        print("Invalid choice. Enter 1 or 2 only.")
    
    print("Your Shopping List")
    for i in range(len(items)):
        print(str(i+1) + ".", items[i])