import random, time

player_score = 0
computer_score = 0

for i in range(1, 11):
    print("Round", i)
    print("Player is rolling the dice...")
    time.sleep(1.5)
    player = random.randint(1, 6)
    print(player)

    print("Computer is rolling the dice...")
    time.sleep(1.5)
    computer = random.randint(1, 6)
    print(computer)

    player_score += player
    computer_score += computer
    print("Player's score:", player_score)
    print("Computer's score:", computer_score)
    print()

if player_score < computer_score:
    print("Computer wins!")
elif player_score > computer_score:
    print("Player wins!")
else:
    print("It's a tie!")