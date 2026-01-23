import random
tries = 10
print("You have", tries, "tries")
number = random.randint(1, 100)
# print(number)
win = False
for i in range(tries):
    print("Attempt", i+1)
    guess = int(input("Guess a number between 1 and 100: "))
    # print(guess)

    if guess > number:
        print("Too high. Guess lower")
    elif guess < number:
        print("Too low. Guess higher")
    else:
        print("You guessed correctly!")
        win = True
        break

if win == False:
    print("You lost. The number was", number)