
def cipher(msg, key, encode=True):
    if encode == True:
        direction = 1
    else:
        direction = -1
    
    result = ""
    for char in msg:
        ascii = ord(char)
        ascii += (key * direction)
        letter = chr(ascii)
        result += letter
    
    return result

def main():
    encoded = ""
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            message = input("Enter your message to encode: ").strip()
            key = int(input("Enter a key for encoding (0-25): ").strip())
            encoded = cipher(message, key)
            print("Your encoded message is", encoded)
        
        elif choice == "2":
            if encoded:
                option = input("Decode previously encoded message? (y/n) ")
                if option == "y":
                    decoded = cipher(encoded, key, encode=False)
                    print("Your decoded message is", decoded)
                    print()
                    continue
            
            message = input("Enter your message to decode: ").strip()
            key = int(input("Enter your key for decoding (0-25): ").strip())
            decoded = cipher(message, key, encode=False)
            print("Your decoded message is", decoded)
            
        elif choice == "3" or choice.lower() == "q":
            print("Thanks for playing!")
            quit()
        
        print()

main()