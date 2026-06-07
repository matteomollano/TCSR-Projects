lst = ["apples", "lettuce", "cheese"]

# add a new item
lst.append("soda")

print(lst)

# remove an item
lst.remove("apples")
print(lst)

while True:
    choice = input("Add or remove (1/2): ")
    if choice == "1":
        item = input("Add: ")
        lst.append(item)
    elif choice == "2":
        item = input("Remove: ")
        try:
            lst.remove(item)
        except:
            print("Item doesn't exist")
    print(lst)
    print()