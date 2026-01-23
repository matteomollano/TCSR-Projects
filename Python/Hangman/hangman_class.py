import random
words = ["apple", "nathaniel", "computer", "skyscraper", "volcano"]
random_word = random.choice(words)
print(random_word)

# create underscores
num_letters = len(random_word)

underscores = []
for i in range(num_letters):
    if random_word[i] == " ":
        underscores.append(" ")
    else:
        underscores.append("_")
# print(underscores)
x = " ".join(underscores)
print(x)

guesses = 6
previous_letters = set()
win = False

while guesses > 0:
    guess = input("Guess a letter: ")
    
    if len(guess) != 1:
        print("Your guess must be 1 letter only")
        continue
    
    if guess in previous_letters:
        print("You already guessed that letter")
        continue
    
    previous_letters.add(guess)
    
    guessed = False
    for i in range(num_letters):
        if random_word[i] == guess: # guess letter correctly
            underscores[i] = guess
            guessed = True
    
    x = " ".join(underscores)
    print(x)
    
    if guessed == False:
        guesses = guesses - 1
        
    # check if no more underscores left
    if "_" not in underscores:
        print("You won!")
        win = True
        break
    
if win == False:
    print("The word was", random_word)