import random

options = ["rock", "paper", "scissors"]

player_score = 0
cpu_score = 0

while True:
    cpu = random.choice(options)
    
    player = input("Enter rock, paper, or scissors: ")
    
    if player not in options:
        print("You must enter rock, paper, or scissors only.")
    else:
        print("CPU chose", cpu)

        if cpu == "rock":
            if player == "paper":
                print("You win")
                player_score += 1
            elif player == "rock":
                print("Draw")
            elif player == "scissors":
                print("You lose")
                cpu_score += 1

        if cpu == "paper":
            if player == "scissors":
                print("You win")
                player_score += 1
            elif player == "paper":
                print("Draw")
            elif player == "rock":
                print("You lose")
                cpu_score += 1

        if cpu == "scissors":
            if player == "rock":
                print("You win")
                player_score += 1
            elif player == "scissors":
                print("Draw")
            elif player == "paper":
                print("You lose")
                cpu_score += 1
        
        print("Computer", cpu_score, "-", player_score, "Player")
        
        if player_score == 3:
            print("Game over. You win")
            break
        
        if cpu_score == 3:
            print("Game over. You lose")
            break
