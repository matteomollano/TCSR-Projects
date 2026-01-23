# class = blueprint
# object = thing you make from blueprint/class

class VirtualPet:
    
    # constructor - function that builds the object
    # init = initialize
    def __init__(self, name):
        # class variable
        self.name = name
        self.hunger = 5
        self.happiness = 5
    
    # we want to decrease hunger by 1
    def feed(self):
        self.hunger = max(0, self.hunger - 1) # get maximum between 0 and negative value
    
    # we want to increase happiness by 1
    # and decrease hunger by 1
    def play(self):
        self.happiness = min(10, self.happiness + 1)
        self.hunger = min(10, self.hunger + 1)
    
    def status(self):
        print(self.name + "'s Status")
        print("Hunger:", self.hunger)
        print("Happiness:", self.happiness)
        

pet = VirtualPet("Cooper")
# print(pet.name)
# print(pet.hunger)
# print(pet.happiness)
pet.play()
pet.status()
pet.feed()
pet.status()