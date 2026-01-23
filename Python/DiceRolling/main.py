import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

rounds = 5
player_score = 0
computer_score = 0

print("Welcome to Dice Roller!")
print("We will play", rounds, "rounds. Guess the sum of two dice (2-12)\n")

for round_num in range(1, rounds+1):
    print("Round", round_num)
    
    # player guess
    player_guess = int(input("Guess the sum (2-12): "))
    
    # computer guess
    computer_guess = random.randint(2, 12)
    print("The computer guessed", computer_guess)
    
    # roll the dice
    total = roll_dice()
    print("The total was", total)
    
    if player_guess == total:
        print("You guessed correctly!")
        player_score += 1
    else:
        print("You missed this round")
        
    if computer_guess == total:
        print("Computer guessed correctly!")
        computer_score += 1
    else:
        print("The computer missed this round")
    
    print("Your score:", player_score)
    print("Computer score:", computer_score)
    print()

print("Final Results")
if player_score > computer_score:
    print("You win", player_score, "-", computer_score)
elif computer_score > player_score:
    print("Computer wins", computer_score, "-", player_score)
else:
    print("You tie", player_guess, "-", computer_score)