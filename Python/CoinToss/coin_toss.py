import random

faces = ["heads", "tails"]
game_playing = True

wins = 0
losses = 0

while game_playing == True:
    computer = random.choice(faces)
    guess = input("Please enter heads or tails: ").lower()
    
    # heads is thrown and you guess heads
    if computer == "heads" and (guess == "head" or guess == "heads"):
        print(f"You guessed {guess} and the computer chose {computer}. Good job!")
        wins += 1
    
    # tails is thrown and you guess tails 
    elif computer == "tails" and (guess == "tail" or guess == "tails"):
        print(f"You guessed {guess} and the computer chose {computer}. Good job!")
        wins += 1
    
    # heads is thrown and you guess tails
    elif computer == "heads" and (guess == "tail" or guess == "tails"):
        print(f"You guessed {guess} and the computer chose {computer}. Unlucky!")
        losses += 1
    
    # tails is thrown and you guess heads
    elif computer == "tails" and (guess == "head" or guess == "heads"):
        print(f"You guessed {guess} and the computer chose {computer}. Unlucky!")
        losses += 1
        
    else:
        print("You entered an incorrect value")
        throw = input("Do you wish to throw again? (y/n) ").lower()
    
        if throw == "yes" or throw == "y":
            continue
        else:
            break
            
    print(f"\nNumber of wins = {wins}")
    print(f"Number of losses = {losses}\n")
    
    throw = input("Do you wish to throw again? (y/n) ").lower()
    
    if throw == "yes" or throw == "y":
        game_playing = True
    else:
        game_playing = False