import random

# get a random word from our word list
with open("words.txt", "r") as file:
    all_text = file.read()
    words = all_text.split()
    random_word = random.choice(words)
    
# create a set for all correct letters guessed by the user
all_correct_letters = set()
guessed = False

def get_guess():
    guess = ""
    while len(guess) != 5:
        guess = input("Guess a random word: ")
        if len(guess) < 5:
            print("Word is too short. Please enter a 5 letter word\n")
        if len(guess) > 5:
            print("Word is too long. Please enter a 5 letter word\n")
    return guess

def show_guess():
    # find the letters in common between the guess and the random word
    current_correct_letters = set(guess) & set(random_word)
    
    # add these letters to the all letters set
    for letter in current_correct_letters:
        all_correct_letters.add(letter)
       
    # tell the user which letters they guessed correctly (for this round and all rounds) 
    if len(current_correct_letters) == 0:
        print("Letters guessed correctly this round:", "{}")
    else:
        print("Letters guessed correctly this round:", current_correct_letters)
        
    if len(all_correct_letters) == 0:
        print("All letters guessed correctly:", "{}")
    else:
        print("All letters guessed correctly:", all_correct_letters)
    
print("-----------------------------------")
print("\tWelcome to Wordle!")
print("-----------------------------------")
print()

# get input from the user
for guess_number in range(1, 7):
    print(f"{guess_number}. ", end="")
    guess = get_guess()
    if guess.lower() == random_word.lower():
        print("Good job! You guessed the word!")
        guessed = True
        break
    else:
        print("That's the wrong word!")
        show_guess()
    print()
    
if guessed == False:
    print("Nice try. The correct word was", random_word)