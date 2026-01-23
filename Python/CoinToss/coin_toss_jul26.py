import random

score = 0

while True: 
    guess = input("Guess the outcome (heads or tails) or type quit to exit: ")
    faces = ["heads", "tails"]
    idx = random.randint(0, 1)
    cpu = faces[idx]
    
    if guess == "quit":
        break
    elif guess not in faces:
        print("Your guess is invalid. Please enter heads or tails only.")
        continue

    if guess == cpu:
        print("You guessed correctly. 1 point will be added to your score.")
        score += 1
    else: # guess != cpu
        print("Sorry, you guessed incorrectly. Try again next time.")
        
    print(f"Your score: {score}\n")