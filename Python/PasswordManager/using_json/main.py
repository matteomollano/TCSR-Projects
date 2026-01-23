import json
from datetime import datetime
from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.pem", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    with open("key.pem", "rb") as key_file:
        key = key_file.read()
    return key

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open('passwords.jsonl', 'r') as f:
            data = f.readlines()
            if data == []:
                print("No passwords saved")
            else:
                for line in data:
                    entry = json.loads(line)
                    url = entry['url']
                    username = entry['username']
                    password = fer.decrypt(entry['password']).decode()
                    created_at = entry['created_at']
                    updated_at = entry['updated_at']
                    notes = fer.decrypt(entry['notes']).decode()
                    print(f"Account: {url}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    print(f"Created: {created_at}")
                    print(f"Updated: {updated_at}")
                    print(f"Notes: {notes}")
                    print("-" * 40)
    except FileNotFoundError:
        print("File not found")
        
def check_existing_entry(url):
    # Load all entries
    entries = []
    try:
        with open('passwords.jsonl', 'r') as f:
            for line in f.readlines():
                entries.append(json.loads(line))
    except FileNotFoundError:
        pass # No file yet, we'll create it later if needed
    
    existing_entry = None
    for entry in entries:
        if entry['url'] == url:
            found = entry
            break
    return existing_entry

def add():
    url = input("Website URL: ").strip().lower()
    username = input("Username/email: ").strip().lower()
    password = input("Password: ").strip().lower()
    time = datetime.now().isoformat()
    notes = input("Notes (Optional): ")
    
    encrypted_password = fer.encrypt(password.encode()).decode()
    encrypted_notes = fer.encrypt(notes.encode()).decode()
    
    json_data = {
        "url": url,
        "username": username,
        "password": encrypted_password,
        "created_at": time,
        "updated_at": time,
        "notes": encrypted_notes
    }
    
    with open('passwords.jsonl', 'a') as f:
        f.write(json.dumps(json_data) + '\n')
    print("Password added successfully (JSON line format)!")
    

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