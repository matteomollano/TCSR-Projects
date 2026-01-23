import random

number = random.randint(1, 100)
# print(number)
win = False
for i in range(3):
    user_input = int(input("Enter a number between 1 and 100: "))

    if user_input == number:
        print("Correct")
        win = True
        break
    elif user_input > number:
        print("Too high. Guess lower")
    elif user_input < number:
        print("Too low. Guess higher")

if win == False:
    print("You lose. The correct number was", number)
else:
    print("Congratulations. You win!")