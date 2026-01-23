import csv

ADDRESS_BOOK_FILE = "address_book.csv"

def add_contact():
    name = input("Enter your name: ").strip()
    address = input("Enter your address: ").strip()
    phone = input("Enter your phone number: ").strip()
    birthday = input("Enter your birthday: ").strip()
    
    with open(ADDRESS_BOOK_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, address, phone, birthday])
    print(f"Successfully added {name} to your contacts")

def view_contacts():
    # read mode
    with open(ADDRESS_BOOK_FILE, "r") as file:
        reader = csv.reader(file)
        contacts = list(reader)
        
        print("Your Contacts")
        print("-" * 40)
        for contact in contacts:
            name = contact[0]
            address = contact[1]
            phone = contact[2]
            birthday = contact[3]
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Phone: {phone}")
            print(f"Birthday: {birthday}")
            print("-" * 40)     

def search_contacts():
    search_name = input("Enter a name to search: ").strip().lower() # "Matteo     " -> "Matteo" -> "matteo"
    with open(ADDRESS_BOOK_FILE, "r") as file:
        reader = csv.reader(file)
        contacts = list(reader)
        
        found = False
        for contact in contacts:
            name = contact[0]
            if search_name in name.lower():
                found = True
                print(f"Found a contact for {search_name}")
                print(f"Name: {name}")
                print(f"Address: {contact[1]}")
                print(f"Phone: {contact[2]}")
                print(f"Birthday: {contact[3]}")
                break
        if not found:
            print(f"No contact found for {search_name}")
                
def address_book_app():
    pass

if __name__ == "__main__":
    search_contacts()