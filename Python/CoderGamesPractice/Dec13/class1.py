def question9():
    """
    9. Hide Credit Card Number
    Ask the user to enter a 16 digit credit card number (add validation to ensure the input is the right length and no letters
    Replace all digits but the last 4 with asterisks (*)
    Display the new credit card number
    """
    card = input("Enter your credit card number: ")
    # substring / string slice
    # print(card[12:])
    # print(card[-4:])
    print("*" * 12 + card[-4:])
    
question9()