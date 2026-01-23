import random

GREEN = '\033[42m'
YELLOW = '\u001b[43m'
RESET = '\033[0m'

# generate random 5-digit number
number = random.randint(10000, 99999)

num_guesses = 6

print("Welcome to 5-digit Guess. You have 6 attempts!")

while num_guesses > 0:
    # get input from user
    guess = input("Enter a 5 digit number: ")
    while len(guess) != 5 or not guess.isnumeric():
        guess = input("Please enter a valid 5 digit number only: ")
        
    # check if they guessed any digits correctly
    number_str = str(number)

    matched_number = []

    for i in range(5):
        if number_str[i] == guess[i]: # guessed correctly and in right spot
            matched_number.append(f"{GREEN}{guess[i]}{RESET}")
        elif number_str[i] != guess[i] and guess[i] in number_str: # guessed correctly but wrong spot
            matched_number.append(f"{YELLOW}{guess[i]}{RESET}")
        else:
            matched_number.append(guess[i])

    print("".join(matched_number))
    
    num_guesses -= 1
    
    if number_str == guess:
        print("You win!")
        break

if num_guesses == 0:
    print(f"You lose. The number was {number}")