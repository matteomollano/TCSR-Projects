class VirtualPet:
    
    # Constructor / Initializer
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        
    def feed(self):
        self.hunger -= 1
        self.happiness += 0.2
    
    def play(self):
        self.happiness += 1
        self.hunger += 1
    
    def status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Happiness: {self.happiness}/10")
    
    # happiness <= 0 or hunger >= 10
    def is_game_over(self):
        # if self.happiness <= 0 or self.hunger >= 10:
        #     return True
        # else:
        #     return False
        return self.happiness <= 0 or self.hunger >= 10
    
# --- Main Game ---
name = input("What would you like to name your pet?")
pet = VirtualPet(name)

while not pet.is_game_over():
    pet.status()
    print("What would you like to do?")
    print("1. Feed")
    print("2. Play")
    print("3. Do nothing")
    
    choice = input("Enter 1, 2, or 3: ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Please enter 1, 2, or 3 only: ").strip()
    if choice == "1":
        pet.feed()
    elif choice == "2":
        pet.play()
    else:
        pet.hunger += 1
        pet.happiness -= 1