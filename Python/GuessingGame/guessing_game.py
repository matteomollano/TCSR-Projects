import random
game_playing = True

total_attempts = 10
attempts_used = 0

number = random.randint(1,100)

def isNumber(number):
    while number.isdigit() != True:
        number = input("Invalid number. Guess again! ")
    return int(number)
        
while game_playing == True:
    guess = input("\nGuess a number between 1 and 100: ")
    guess = isNumber(guess)
    if (guess == number):
        print("You guessed the number correctly! Nice job!")
        attempts_used += 1
        game_playing = False
    elif (guess < number):
        print("You need to guess higher. Try again")
        attempts_used += 1
        print(f"Attempts remaining: {total_attempts - attempts_used}")
    else:
        print("You need to guess lower. Try again")
        attempts_used += 1
        print(f"Attempts remaining: {total_attempts - attempts_used}")
        
    if (game_playing == False):
        play_again = input("Do you want to play again? (y/n) ").lower()
        
        if play_again == "yes" or play_again == "y":
            number = random.randint(1,100)
            game_playing = True
            attempts_used = 0
        else:
            game_playing = False
    
    if (attempts_used >= total_attempts):
        print(f"\nSorry. You used all {total_attempts} attempts!")
        
        play_again = input("Do you want to play again? (y/n) ").lower()
        
        if play_again == "yes" or play_again == "y":
            number = random.randint(1,100)
            game_playing = True
            attempts_used = 0
        else:
            game_playing = False