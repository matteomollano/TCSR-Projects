import random

choices = ["rock", "paper", "scissors"]
again = "yes"

while again == "yes" or again == "y":

    player = input("Enter rock, paper, or scissors: ").strip().lower()
    while player not in ["rock", "paper", "scissors"]:
        print("You must enter rock, paper, or scissors.")
        player = input("Enter choice: ").strip().lower()
    
    cpu = random.choice(choices)
    print(f"CPU chose {cpu}")
    
    if player == "rock":
        if cpu == "paper":
            print("Computer wins!")
        elif cpu == "scissors":
            print("You win!")
        elif cpu == "rock":
            print("Tie")

    elif player == "paper":
        if cpu == "paper":
            print("Tie!")
        elif cpu == "scissors":
            print("Computer wins!")
        elif cpu == "rock":
            print("Player wins!")
            
    elif player == "scissors":
        if cpu == "paper":
            print("You win!")
        elif cpu == "scissors":
            print("Tie")
        elif cpu == "rock":
            print("Computer wins!")
    
    again = input("Do you want to play another round? (yes/no) ")
    if again == "yes" or again == "y":
        print()