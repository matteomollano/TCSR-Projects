import random

with open("words.txt", "r") as file:
    all_words = file.read()
    word_list = all_words.split()
    random_word = random.choice(word_list)

all_correct_letters = set()
guessed = False

for i in range(1,7):
    print(str(i)+". ", end="")
    guess = input("Please enter a 5-letter word: ").lower()
    if guess == random_word:
        print("Great job! You guessed the correct word!")
        guessed = True
        break
    else:
        print("You guessed the wrong word")
        # find the letters in common between the guess and the random word
        current_correct_letters = set(guess) & set(random_word)
        
        for letter in current_correct_letters:
            all_correct_letters.add(letter)
        
        if len(current_correct_letters) == 0:
            print("Letters guessed correctly this round:", "None")
        else:
            print("Letters guessed correctly this round:", current_correct_letters)
            
        if len(all_correct_letters) == 0:
            print("All letters guessed correctly:", "None")
        else:
            print("All letters guessed correctly:", all_correct_letters)
    print()
    
if guessed == False:
    print("Nice try! The correct word was", random_word)