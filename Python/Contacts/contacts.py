contacts = {}

while True:
    print("1. Add contact")
    print("2. Update contact")
    print("3. Remove contact")
    print("4. Display")
    print("5. Quit")
    
    choice = input("Your choice (1-5): ")
    if choice == "1":
        name = input("What would you like the name to be? ")
        phone = input("What about the phone number? ")
        contacts[name] = phone
    
    elif choice == "2":
        name = input("Whose number do you want to change? ")
        if name in contacts:
            new_phone = input("Enter the new number: ")
            contacts[name] = new_phone
        else:
            print(name, "is not in your contacts")
    
    elif choice == "3":
        name = input("Who do you want to remove? ")
        if name in contacts:
            contacts.pop(name)
        else:
            print(name, "is not in your contacts")
    
    elif choice == "4":
        print("=" * 30)
        print(" " * 10, "Contacts")
        print("=" * 30)
        for key, value in contacts.items():
            print(key, "-", value)
    
    elif choice == "5":
        break
    
    else:
        print("You must enter 1-5 only.")
