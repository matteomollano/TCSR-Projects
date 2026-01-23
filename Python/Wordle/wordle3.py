import random

words = ['apple', 'toast', 'board', 'flyer', 'cloud', 'range', 'local', 'train', 'merit', 'quick', 'metal', 'bread', 'vital', 'visit']

GREEN = '\033[42m'
# YELLOW = '\033[43m'
YELLOW = '\u001b[43m'
RESET = '\033[0m'

def get_guess():
    guess = input("Enter a 5-letter word: ")
    while len(guess) != 5 or not guess.isalpha():
        guess = input("Invalid word. Enter 5 letters only: ")
    return guess

def match_guess(random_word, user_guess): 
    matched_word = []
    
    for i in range(len(random_word)):
        if random_word[i] == user_guess[i]:
            matched_word.append(f'{GREEN}{user_guess[i]}{RESET}')
            # matched_word.append(GREEN+user_guess[i]+RESET)
        elif user_guess[i] in random_word and random_word[i] != user_guess[i]:
            matched_word.append(f'{YELLOW}{user_guess[i]}{RESET}')
        else:
            matched_word.append(user_guess[i])
 
    return ''.join(matched_word)

def check_for_win(random_word, user_guess):
    return random_word == user_guess
    
random_word = random.choice(words)
# print(random_word)

for i in range(6):
    user_guess = get_guess()
    matched_guess = match_guess(random_word, user_guess)
    print(matched_guess)
    
    if check_for_win(random_word, user_guess):
        print("You win!")
        break
    
if not check_for_win(random_word, user_guess):
    print("The word was", random_word)