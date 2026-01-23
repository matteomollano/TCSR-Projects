
def caesar_cipher(msg, key, encode=True):
    if encode == True:
        direction = 1
    else: # encode = False
        direction = -1
        
    result = ""
    for char in msg:
        if char.isalpha(): # is in the alphabet
            if char.isupper(): # is uppercase letter
                base = 65
            else:
                base = 97
            
            # convert to ASCII
            ascii_number = ord(char)
            index = ascii_number - base
            shifted_index = index + (key * direction)
            wrapped_index = shifted_index % 26
            new_char = chr(wrapped_index + base)
            
            result += new_char
        else:
            result += char # just add punctuation, numbers, and spaces
    return result
            
# encoded = caesar_cipher("apple", 6)
# print(encoded)
while True:
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("Choose an option (1-3): ").strip()
    
    if choice == "3":
        print("Thanks for playing!")
        break
    
    if choice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3 only.")
        continue
    
    key = int(input("Enter a key for encoding (0-25): "))
    if choice == "1":
        msg = input("Enter a message to encode: ")
        encoded = caesar_cipher(msg, key)
        print("Your encoded message (copy this exactly!)")
        print(encoded)
    elif choice == "2":
        msg = input("Enter a message to decode: ")
        decoded = caesar_cipher(msg, key, encode=False)
        print("Your decoded message:", decoded)
    print()