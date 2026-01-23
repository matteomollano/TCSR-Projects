from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.pem", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.pem", "rb") as key_file:
        key = key_file.read()
    return key