import random

WORDS = ["apple", "snake", "quiz", "cheese", "elevator", "skyscraper", "chicken", "nighttime", "volcano", "computer"]

random_word = random.choice(WORDS)
print(random_word)

empty_word = []
for i in range(len(random_word)):
    empty_word.append("_")
    
empty_string = " ".join(empty_word)
print(empty_string)

guesses = 6

letters_used = set()

while guesses > 0:
    print("Guesses left:", guesses)
    guess = input("Enter a letter: ")
    while len(guess) > 1 or not guess.isalpha() or guess in letters_used:
        guess = input("Invalid input. Enter a letter: ")
    letters_used.add(guess)

    is_guessed = False
    for i in range(len(random_word)):
        # print(f"if {random_word[i]} == {guess}")
        if random_word[i] == guess:
            empty_word[i] = guess
            is_guessed = True
    
    if is_guessed == False:
        guesses = guesses - 1
        
    print(" ".join(empty_word))
    
    if "_" not in empty_word:
        print("You win!")
        break

if guesses == 0:
    print("You lose. The word was", random_word)