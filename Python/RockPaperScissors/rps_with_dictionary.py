import random

computer_options = ["rock", "scissors", "paper"]

win_conditions = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}

computer_score = 0
user_score = 0

while True:
    computer = random.choice(computer_options)
    user = ""
    while user not in ["rock", "paper", "scissors"]:
        user = input("Enter rock, paper, or scissors: ").lower()
        
    if user == computer:
        print(f"The user and computer both chose {user}. It's a tie!")
    else:
        if win_conditions[user] == computer:
            print(f"The user chose {user} and the computer chose {computer}")
            print("The user wins!")
            user_score += 1
        else:
            print(f"The user chose {user} and the computer chose {computer}")
            print("The computer wins!")
            computer_score += 1
    print(f"Computer score: {computer_score}")
    print(f"User score: {user_score}")
    print()