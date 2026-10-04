import random

choices = ["rock", "paper", "scissors"]

cpu_score = 0
player_score = 0

while True:

    cpu = random.choice(choices)

    player = input("Rock, paper, or scissors? ").lower().strip()

    print("Bot chose", cpu)

    if cpu == player:
        print("It's a draw")
    elif cpu == "rock":
        if player == "paper":
            print("You have beat AI! You become the AI! HAHA")
            player_score = player_score + 1
        elif player == "scissors":
            print("You lost to a bot! L! WOMP WOMP")
            cpu_score = cpu_score + 1
    elif cpu == "paper":
        if player == "rock":
            print("You lost to a bot! L! WOMP WOMP")
            cpu_score = cpu_score + 1
        elif player == "scissors":
            print("You have beat AI! You become the AI! HAHA")
            player_score = player_score + 1
    elif cpu == "scissors":
        if player == "rock":
            print("You have beat AI! You become the AI! HAHA")
            player_score = player_score + 1
        elif player == "paper":
            print("You lost to a bot! L! WOMP WOMP")
            cpu_score = cpu_score + 1

    print(f"CPU {cpu_score} - {player_score} Player\n")
