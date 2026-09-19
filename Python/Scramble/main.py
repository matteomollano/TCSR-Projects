import random

words = ["triangle", "purple", "dodecagon", "pineapple", "lollipop"]

word = random.choice(words)
# print(word)

word_list = list(word)
random.shuffle(word_list)

scramble = "".join(word_list)
print(scramble)

attempts = 3

while attempts > 0:
    guess = input("Your guess: ").lower().strip()
    
    if guess == word:
        print("Great job!")
        break
    
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong! You have {attempts} attempts left.")
       
if attempts == 0:
    print(f"Out of tries! The correct word was: {word}")
    