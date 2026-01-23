import time

class VirtualPet:
    # Class Constructor / Initializer
    def __init__(self, name):
        self.name = name
        self.hunger = 5     # 0 (not hungry) to 10 (very hungry)
        self.happiness = 5  # 0 (sad) to 10 (happy)

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            print(f"{self.name} is eating. Yum!")
        else: # self.hunger <= 0
            print(f"{self.name} is full.")

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            self.hunger += 1  # playing makes pet hungry
            print(f"{self.name} is playing and having fun!")
        else: # self.happiness >= 10
            print(f"{self.name} is already super happy!")

    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Happiness: {self.happiness}/10\n")

    def is_game_over(self):
        return self.hunger >= 10 or self.happiness <= 0

# --- Main Game ---
name = input("What would you like to name your pet? ")
pet = VirtualPet(name)

print(f"\nWelcome to the Virtual Pet Game! Take care of {name}.")

while not pet.is_game_over():
    pet.status()
    print("What would you like to do?")
    print("1. Feed")
    print("2. Play")
    print("3. Do nothing")

    choice = input("Enter 1, 2 or 3: ").strip() # "1   " -> "1"
    
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Please enter 1, 2, or 3 only: ").strip()

    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        print(f"{name} is waiting...")
        pet.hunger += 1
        pet.happiness -= 1

    time.sleep(1)

print(f"\nGame Over! {name} couldn't survive. Try again next time!")