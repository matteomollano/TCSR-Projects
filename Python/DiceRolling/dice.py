import random

# function is a block of code that will be reused
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

player_score = 0
computer_score = 0

for i in range(5):
    sum = roll_dice()

    player_guess = input("Enter a guess (2-12): ")
    computer_guess = random.randint(2, 12)
    print("Sum:", sum)
    print("Computer guess:", computer_guess)

    if sum == player_guess:
        print("You guessed correctly")
        player_score += 1
    else:
        print("You guessed incorrectly")
        
    if sum == computer_guess:
        print("Computer guessed correctly")
        computer_score += 1
    else:
        print("Computer guessed incorrectly")
        
if player_score > computer_score:
    print("You win", player_score, "-", computer_score)
elif computer_score > player_score:
    print("Computer wins", computer_score, "-", player_score)
else: # draw
    print("It's a tie")