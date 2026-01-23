from datetime import datetime
from key_functions import load_key
from cryptography.fernet import Fernet

key = load_key()
fer = Fernet(key)

# Ask the user to enter their password information
# This should include
# - Website URL
# - Username
# - Password
# - Notes
# These should be stored in 4 separate variables. You can use input() to ask the questions.
def add():
    url = input("Enter a website URL: ")
    encrypted_url = fer.encrypt(url.encode()).decode()
    
    username = input("Enter a username: ")
    encrypted_username = fer.encrypt(username.encode()).decode()
    
    password = input("Enter a password: ")
    encrypted_password = fer.encrypt(password.encode()).decode()
    
    notes = input("Enter some notes (Optional): ")
    encrypted_notes = fer.encrypt(notes.encode()).decode()
    
    date = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    encrypted_date = fer.encrypt(date.encode()).decode()
    
    info = f"{encrypted_url},{encrypted_username},{encrypted_password},{encrypted_notes},{encrypted_date}\n"
    with open("passwords.txt", "a") as file:
        file.write(info)

def view():
    with open("passwords.txt", "r") as file:
        data = file.readlines()
    print("Your Passwords")
    print("-" * 40)
    for line in data:
        line = line.strip()
        info = line.split(",")
        url = fer.decrypt(info[0]).decode()
        username = fer.decrypt(info[1]).decode()
        password = fer.decrypt(info[2]).decode()
        notes = fer.decrypt(info[3]).decode()
        date = fer.decrypt(info[4]).decode()
        print(f"Website URL: {url}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Notes: {notes}")
        print(f"Date Created: {date}")
        print("-" * 40)
        
def main():
    while True:
        mode = input("Add a new password (1), view existing passwords (2), or q to quit: ").lower().strip()
        while mode not in ["1", "2", "q"]:
            mode = input("Invalid input. Enter 1, 2, or q only: ").lower().strip()
        if mode == "q":
            break
        
        if mode == "1":
            add()
        elif mode == "2":
            view()
            
        print()
        
if __name__ == "__main__":
    main()