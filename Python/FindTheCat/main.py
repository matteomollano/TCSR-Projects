import random

print("Find the Cat!")
cats = []

while True:
    cat = random.randint(1, 3)

    print("📦 1     📦 2     📦 3")
    guess = input("Which box is the cat in? (Enter q to quit): ").lower().strip()

    while guess not in ["1", "2", "3", "q"]:
        guess = input("Enter 1, 2, 3, or q only: ").lower().strip()

    if guess == "q":
        num_cats = len(cats)
        if num_cats == 1:
            print(f"You found {num_cats} cat!")
        else:
            print(f"You found {num_cats} cats!")
        if num_cats > 0:
            print(cats)
        break

    guess = int(guess)

    if guess == cat:
        print("You found the cat! 🐈\n")
        cats.append("🐈")
    else:
        print(f"Incorrect. The cat was in box {cat}\n")
