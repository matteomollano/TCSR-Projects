from english_words import get_english_words_set
import random
import math
# import json
# import pandas as pd

words = list(get_english_words_set(['web2'], alpha=True, lower=True))

# data analysis of word list
character_occurrence = dict()
for word in words:
    length = len(word)
    if length not in character_occurrence:
        character_occurrence[length] = 1
    else:
        character_occurrence[length] += 1

# print(json.dumps(character_occurrence, indent=4))

# dataframe = pd.DataFrame(list(character_occurrence.items()), columns=['Length', 'Occurrence'])
# dataframe.sort_values(by='Length', inplace=True)
# print(dataframe)


# get difficulty level and perform input validation
while True:
    try:
        characters = int(input("Select your difficulty level, in terms of the number of characters (2-24, or 28): "))
        if characters in range(2, 25) or characters == 28:
            break  # Exit loop if valid input
        else:
            print("Invalid choice. Enter a number between 2 and 24, or 28.")
    except ValueError:
        print("Please enter a valid integer.")


# get the random word
word_list = []
for word in words:
    if len(word) == characters:
        word_list.append(word)
       
random_word = random.choice(word_list) 
# print(random_word)

# create an empty word list to keep track of the user's guesses
empty_word = []
for char in random_word:
    empty_word.append("_")

guessed_letters = set()

guesses = math.ceil(len(random_word) / 2)

while guesses > 0:
    print(f"You have {guesses} guesses left")
    
    # get a guess from the user
    player_guess = input("Enter a letter to guess: ").lower()
    while len(player_guess) != 1 or not player_guess.isalpha() or player_guess in guessed_letters:
        player_guess = input("Invalid choice. Enter a letter: ").lower()
    guessed_letters.add(player_guess)

    # update the empty word list when the user guesses a letter correctly
    for index, char in enumerate(random_word):
        if char == player_guess:
            if empty_word[index] == "_":
                empty_word[index] = player_guess         
    
    if player_guess not in random_word:
        print(f"{player_guess} was incorrect")
        guesses -= 1
    
    print(f"Letters guessed: {", ".join(guessed_letters)}")
    print(" ".join(empty_word))
    print()
    
    if "_" not in empty_word:
        print(f"You win! The word was {random_word}")
        break
    
if guesses == 0:
    print(f"You ran out of guesses! The word was {random_word}")