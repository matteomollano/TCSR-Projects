import random

options = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(options)
    player = input("Enter rock, paper, or scissors: ").lower()
    
    while player not in options:
        print("You entered invalid input.")
        player = input("You have to enter rock, paper, or scissors: ").lower()

    if computer == "rock" and player == "scissors":
        print("Computer chose", computer, "and player chose", player)
        print("Computer wins!")
    elif computer == "rock" and player == "paper":
        print("Computer chose", computer, "and player chose", player)
        print("Player wins!")
    elif computer == "paper" and player == "scissors":
        print("Computer chose", computer, "and player chose", player)
        print("Player wins!")
    elif computer == "paper" and player == "rock":
        print("Computer chose", computer, "and player chose", player)
        print("Computer wins!")
    elif computer == "scissors" and player == "paper":
        print("Computer chose", computer, "and player chose", player)
        print("Computer wins!")
    elif computer == "scissors" and player == "rock":
        print("Computer chose", computer, "and player chose", player)
        print("Player wins!")
    else:
        print("Computer chose", computer, "and player chose", player)
        print("Draw!")
    print()