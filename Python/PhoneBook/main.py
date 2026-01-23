
# class = way to represent real-world object
class PhoneBook:
    
    # class constructor / initializer
    def __init__(self):
        self.dictionary = {}
        
    def addContact(self, name, number):
        if name in self.dictionary.keys():
            choice = ""
            while (choice != "y" and choice != "n"):
                choice = input(f"You already have a contact for {name}. \nAre you sure you want to update it? (y/n): ").lower()
            
            if choice == "y":
                self.dictionary[name] = number
                
        else:
            self.dictionary[name] = number
        
    def deleteContact(self, name):
        if name in self.dictionary.keys():
            self.dictionary.pop(name)
        else:
            print(f"You do not have a contact for {name}")
        
    def display(self):
        if not self.dictionary:
            print("Your phone book is empty")
        else:
            for name, number in self.dictionary.items():
                print(f"{name} -> {number}")
        
    
pb = PhoneBook()
while True:
    
    choice = int(input(
        """What would you like to do?
        1) Display phonebook
        2) Add a new contact
        3) Delete a contact
        Enter your selection: """
    ))
    
    while (choice not in [1, 2, 3]):
        choice = int(input("Invalid selection. Please choose 1, 2, or 3 only"))
        
    if choice == 1:
        print("\nDisplaying Phone Book")
        pb.display()
    elif choice == 2:
        print("\nAdding New Contact")
        name = input("Enter a name: ")
        number = input("Enter their number: ")
        pb.addContact(name, number)
    else:
        print("\nDeleting Contact")
        name = input("Enter the name for the contact you want to delete: ")
        pb.deleteContact(name)
        
    print()
    
    
# pb = PhoneBook()
# print("New phone book")
# pb.display()

# print("\nAftering adding some contacts")
# pb.addContact("Michael", "123-456-7890")
# pb.addContact("Matteo", "457-3514-1451")
# pb.addContact("Justin", "123-4521-1325")
# pb.addContact("Justin", "245-1345-5858")
# pb.display()

# print("\nDeleting Matteo from phone book")
# pb.deleteContact("Matteo")
# pb.deleteContact("Matteo")
# pb.display()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index-based for loop
# for i in range(len(numbers)):
#     print(numbers[i])
    
# for-each loop
# for number in numbers:
#     print(number)