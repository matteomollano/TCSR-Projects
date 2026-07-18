import random

movies = ["Minions & Monsters", "Toy Story 5", "The Odyssey", "Backrooms", "Project Hail Mary"]

random_movie = random.choice(movies).lower()

underscores = []
for letter in random_movie:
    if letter != " ":
        underscores.append("_")
    else:
        underscores.append(" ")

print(" ".join(underscores))

num_guesses = 7
guessed = []

while num_guesses > 0:
    pick_letter = input("Pick a letter: ").strip().lower()
    
    if pick_letter in guessed:
        print(f"You already guessed {pick_letter}")
        continue
    
    guessed.append(pick_letter)
    
    if pick_letter not in random_movie:
        num_guesses -= 1
    
    for i in range(len(random_movie)):
        # print(f"[{i}] if {random_movie[i]} == {pick_letter}")
        if random_movie[i] == pick_letter:
            underscores[i] = pick_letter
    print(" ".join(underscores))
    
    print(f"You still have {num_guesses} guesses remaining")
    
    if underscores == list(random_movie):
        print("You win!")
        break

if num_guesses == 0:
    print(f"You lose! The correct answer was {random_movie}")
