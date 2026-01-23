
def caesar_cipher(text, shift, encode=True):
    result = ""
    if encode:
        direction = 1
    else:
        direction = -1 # shift backwards (decode)
        
    for char in text:
        if char.isalpha(): # if char is in the alphabet
            # Determine ASCII base for uppercase or lowercase
            if char.isupper():
                base = 65 # A is 65, B is 66, C is 67
            else:
                base = 97 # a is 97, b is 98, c is 99

            # Normalize, shift, wrap, and convert back
            char_index = ord(char) - base
            shifted_index = char_index + (direction * shift)
            wrapped_index = shifted_index % 26
            new_char = chr(wrapped_index + base) # convert back to ASCII char

            # append new char to the result
            result += new_char
        else:
            result += char  # punctuation, spaces, numbers

    return result

# UI
print("Welcome to Message Cipher")
print("-" * 25)

while True:
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("Choose an option (1-3): ")
    
    if choice == "3":
        print("Thanks for playing")
        break
    
    if choice not in ["1", "2"]:
        print("Please type 1, 2, or 3 only.")
        continue
    
    key = int(input("Enter a secret key number (1-25): "))
    while not 1 <= key <= 25:
        print("Key must be 1-25.")
        key = int(input("Enter a secret key number (1-25): "))
    
    if choice == "1":
        message = input("Enter your secret message: ")
        coded = caesar_cipher(message, key)
        print("\nYour encoded message (copy this exactly!):")
        print(coded)
    else:
        coded = input("Enter your encrypted message here: ")
        decoded = caesar_cipher(coded, key, encode=False)
        print("\nDecoding...")
        print("Original message:", decoded)
    print()