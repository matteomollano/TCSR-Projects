import csv

# write using csv writer
with open("address_book.txt", "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Joe", "Roslyn", "4581340584"])
    
# view
with open("address_book.txt", "r") as file:
    reader = csv.reader(file)
    contacts = list(reader)
    
    for contact in contacts:
        print(f"Name: {contact[0]}")
        print(f"Address: {contact[1]}")
        print(f"Phone: {contact[2]}")
        print("-" * 40)
        
# search
with open("address_book.txt", "r") as file:
    search_name = input("Enter a name to search: ").lower().strip()
    contacts = csv.reader(file)
    found = False
    for contact in contacts:
        if search_name in contact[0].lower():
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            found = True
            break
    if not found:
        print("No contact found with that name.")