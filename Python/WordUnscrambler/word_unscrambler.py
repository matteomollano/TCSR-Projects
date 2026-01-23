import random

# function = a block of code that will be reused in our code
# parameter = input passed to a function
def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    print("".join(letters))

# scramble_word("python")
words = ["python", "geometry", "space", "soccer", "anemone", "innovation", "parameter", "fireplace", "reference", "euphemism", "amazing"]
# index = random.randint(0, len(words)-1)
# random_word = words[index]
random_word = random.choice(words)

scrambled = scramble_word(random_word)
print(scrambled)

while True:
    guess = input("Your guess: ").lower().strip()
    
    while len(scrambled) != len(guess):
        print(f"Your guess must be {len(scrambled)} letters")
        guess = input("Your guess: ").lower().strip()
        
    if random_word == guess:
        print("You guessed correctly")
        break
    else:
        feedback = []
        for i in range(len(random_word)):
            if random_word[i] == guess[i]:
                feedback.append("\033[42m" + guess[i] + "\033[0m") # update to make green
            else: # letters are not equal
                feedback.append(guess[i])
        print("".join(feedback))