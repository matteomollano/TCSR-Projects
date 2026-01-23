import requests

# get random word
url = "https://random-word-api.herokuapp.com/word"
response = requests.get(url)
word = response.json()[0]
print(word)

# instantiate empty word list
empty_word = []
for i in range(len(word)):
    empty_word.append("_")

empty_string = " ".join(empty_word)
print(empty_string)

# set up main game loop
guesses = 7

while guesses > 0 and "_" in empty_word:
    print(f"You have {guesses} guesses left")
    guess = input("Enter a letter: ")
    while not guess.isalpha() or len(guess) != 1:
        guess = input("Enter 1 letter only: ")

    correct_guess = False
    for i in range(len(word)):
        if word[i] == guess:
            empty_word[i] = guess
            correct_guess = True

    if not correct_guess:
        guesses -= 1
    
    print(" ".join(empty_word))