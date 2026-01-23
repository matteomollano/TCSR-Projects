import random

def main():
    
    # boolean variable to determine if user has guessed the word
    guessed = False
    
    # read content from words.txt and choose a random word
    with open("words.txt", "r") as file:
        word_list = file.read().split("\n")
        word_list = list(map(lambda word: word.upper(), word_list))
        word = random.choice(word_list)
        print(word)
        
    # main loop
    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        guess = validate_guess(guess)
        if guess == word:
            print("Correct")
            guessed = True
            break
        else:
            print("Wrong")
            show_guess(guess,word)
            
    # check if user has won
    if guessed:
        print("\nYou win!")
    else:
        print(f"\nSorry, the correct word was {word}.")

# receives the user's guess and random word
# returns a set listing the correct letters (letters guessed in the right spot)
def correct_letters(guess, word):
    correct_letters_set = set()
    for guess_letter, word_letter in zip(guess,word):
        if guess_letter == word_letter:
            correct_letters_set.add(guess_letter)
    return correct_letters_set

# receives the user's guess, random word, and correct letters list
# returns the set of correctly guessed letter in the wrong spot
def misplaced_letters(guess,word,correct_letters):
    all_correct_letters = set(guess) & set(word)
    return all_correct_letters - correct_letters
    
# receives the user's guess and random word
# returns the set of letters that the user guessed wrong
def wrong_letters(guess,word):
    return set(guess) - set(word)

# validate the user's guess
def validate_guess(guess):
    while len(guess) != 5:
        if len(guess) < 5:
            print("Word is too short. Please enter a 5 letter word\n")
        if len(guess) > 5:
            print("Word is too long. Please enter a 5 letter word\n")
        guess = input("Guess a random word: ")
    return guess.upper()

# display guess analysis to the user
def show_guess(guess,word):
    """Show the user's guess on the terminal and classify all letters.

    ## Example (with expected output):
    
    >>> show_guess("CRANE", "SNAKE")
    Correct letters: ['A', 'E']
    Misplaced letters: ['N']
    Wrong letters: ['C', 'R']
    """
    correct_letters_set = correct_letters(guess,word)
    misplaced_letters_set = misplaced_letters(guess,word,correct_letters_set)
    wrong_letters_set = wrong_letters(guess,word)
    
    print(f"Correct letters: {sorted(correct_letters_set)}")
    print(f"Misplaced letters: {sorted(misplaced_letters_set)}")
    print(f"Wrong letters: {sorted(wrong_letters_set)}")


if __name__ == "__main__":
    main()