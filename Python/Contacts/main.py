
def add_contact():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    birthday = input("Enter your birthday: ")

    # w = write (over-write previous data)
    # a = append (adds to end of file)
    with open("contacts.txt", "a") as file:
        # Option 1
        string = name + "," + address + "," + phone + "," + birthday + "\n"
        file.write(string)

def read_contacts():
    # r = read
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        # print(line)
        data = line.split(",")
        # print(data)
        
        # index = position in list (number)
        name = data[0]
        address = data[1]
        phone = data[2]
        birthday = data[3]
        print("Name:", name)
        print("Address:", address)
        print("Phone:", phone)
        print("Birthday:", birthday)
        
def search_contacts():
    search_name = input("Enter a name to search: ").strip().lower()
    
    with open("contacts.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        data = line.split(",")
        name = data[0].strip().lower()
        
        if name == search_name:
            name = data[0]
            address = data[1]
            phone = data[2]
            birthday = data[3]
            print("Name:", name)
            print("Address:", address)
            print("Phone:", phone)
            print("Birthday:", birthday)

if __name__ == "__main__":
    pass