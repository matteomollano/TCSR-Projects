import random

words = ['science', 'flower', 'automobile', 'applause', 'bear', 'alive', 'kangaroo', 'fallout', 'effort']

def create_empty_word(random_word):
    empty_word = []
    for char in random_word:
        empty_word.append('_')
    return empty_word

def display(empty_word):
    print(' '.join(empty_word))
    
def get_guess(letters_guessed):
    guess = input("Enter a letter: ").lower()
    while len(guess) != 1 or not guess.isalpha() or guess in letters_guessed:
        guess = input("Invalid input. Enter a letter only: ").lower()
    return guess

def update_empty_word(player_guess, random_word, empty_word):
    for index, char in enumerate(random_word):
        if player_guess == char:
            if empty_word[index] == '_':
                empty_word[index] = player_guess
    return empty_word
        
num_guesses = 7

random_word = random.choice(words)
empty_word = create_empty_word(random_word)

letters_guessed = []

while num_guesses > 0:

    print("You have", num_guesses, "guesses left!")
    display(empty_word)

    player_guess = get_guess(letters_guessed)
    
    letters_guessed.append(player_guess)
    print("Letters guessed: " + ', '.join(letters_guessed))
    
    empty_word = update_empty_word(player_guess, random_word, empty_word)
    
    if player_guess not in random_word:
        num_guesses -= 1
    
    if '_' not in empty_word:
        print("You win! The word is", random_word)
        break
    
    print()

if num_guesses == 0:
    print("The word was", random_word)

'''
bear
_ _ _ _
_ _ a _
'''