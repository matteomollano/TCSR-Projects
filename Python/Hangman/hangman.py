import random

words = ["anything", "science", "english", "kitten", "burger", "fanta", "propensity", "swell", "calculation", "dress to impress"]

random_word = random.choice(words)
# print(random_word)

def create_hangman_list(word):
    hangman_list = []
    for letter in word:
        if letter == ' ':
            hangman_list.append(' ')
        else:
            hangman_list.append('_')   
    return hangman_list

def create_phrase(hangman_list):
    return ' '.join(hangman_list)

def update_hangman_list(hangman_list, indices, guess):
    for i in indices:
        hangman_list[i] = guess
        
def check_for_win(hangman_list):
    # if '_' not in hangman_list:
    #     return True
    # return False
    
    if '_' in hangman_list:
        return False
    else:
        return True

attempts = 7
hangman_list = create_hangman_list(random_word)
hangman_phrase = create_phrase(hangman_list)
letters_guessed = []

while attempts > 0:
    print(f"\nNumber of attempts left: {attempts}")
    print(hangman_phrase)
    guess = input("Guess a letter: ")
    
    if guess in letters_guessed:
        print("You already guessed this letter. Please choose another letter.")
        print(f"Letters already guessed: {', '.join(letters_guessed)}")
        # print("Letters already guessed:", ', '.join(letters_guessed))
        continue
    else:
        letters_guessed.append(guess)
    
    if guess in random_word:
        indices = []
        for i in range(len(random_word)): 
            if random_word[i] == guess: 
               indices.append(i)
        update_hangman_list(hangman_list, indices, guess)
        hangman_phrase = create_phrase(hangman_list)
    else:
        attempts -= 1
    
    # win condition    
    if check_for_win(hangman_list):
        print(f"\nYou win with {attempts} attempts left!")
        # print("You win with", attempts, "attempts left!")
        print(f"The phrase was {random_word}")
        # print("The phrase was", random_word)
        break
    
if not check_for_win(hangman_list):
    print("\nYou lost :(")
    print(f"The phrase was {random_word}")