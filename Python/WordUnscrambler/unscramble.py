import random

GREEN = "\033[42m"
RESET = "\033[0m"
YELLOW = "\u001b[43m"

# function = a block of code that will be reused in our code
# parameter = input passed to a function
def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

# scramble_word("python")
words = ["python", "geometry", "space", "soccer", "anemone", "innovation", "parameter", "fireplace", "reference", "euphemism", "amazing"]

# index = random.randint(0, len(words)-1)
# random_word = words[index]
random_word = random.choice(words)

scrambled = scramble_word(random_word)
print(scrambled)


num_guesses = 3
win = False
for i in range(num_guesses):
    guess = input("Guess the word: ")

    while len(scrambled) != len(guess):
        print("Your guess must be", len(scrambled), "letters")
        guess = input("Guess the word: ")
    
    # at this point, the guess is the right number of letters
    if random_word == guess:
        print("Congrats. You guessed correctly!")
        win = True
        break
    else:
        print("Wrong try again")
        feedback = []
        for i in range(len(random_word)):
            # print(f"if random_word[{i}] -> {random_word[i]} == guess[{i}] -> {guess[i]}")
            if random_word[i] == guess[i]: # letter guessed in right spot
                feedback.append(GREEN + guess[i] + RESET)
            elif random_word[i] != guess[i] and guess[i] in random_word:
                feedback.append(YELLOW + guess[i] + RESET)
            else: # letter not correct
                feedback.append(guess[i])
        print("".join(feedback))
    
    # Vivienne's solution
    # else: # if they're not equal (random_word != guess)
    #     num_guesses = num_guesses - 1
    #     if num_guesses == 0:
    #         print("Sorry maybe next time")
    #         print("The word was", random_word)
    #     else:
    #         print("Wrong try again")
    
if win == False:
    print("Sorry maybe next time")
    print("The word was", random_word)