import random

with open("words.txt", "r") as file:
    all_words = file.read()
    word_list = all_words.split()

random_word = random.choice(word_list)
print(random_word)

print(word_list)
print()
guess = input("Please enter a five letter word from the word list above: ")

if guess == random_word:
    print("Great job! You guessed the word! 😁")
else:
    print("Nice try! You guessed wrong! 🤬")