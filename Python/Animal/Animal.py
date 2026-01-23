
class Animal:
    
    # class constructor
    def __init__(self, species, name, age, color, gender):
        self.species = species
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
    
    # getter and setter methods
    def get_species(self):
        return self.species
    
    # parameter = variable passed to a function
    def set_species(self, new_species):
        self.species = new_species
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
    def get_age(self):
        return self.age
    
    def set_age(self, new_age):
        self.age = new_age
    
    def get_color(self):
        return self.color
        
    def set_color(self, new_color):
        self.color = new_color
    
    def get_gender(self):
        return self.gender
    
    def set_gender(self, new_gender):
        self.gender = new_gender


# Inheritance
class Dog(Animal):
    
    def __init__(self, species, name, age, color, gender, breed):
        Animal.__init__(self, species, name, age, color, gender)
        self.breed = breed
        
    def get_breed(self):
        return self.breed
        
        
dog = Dog("Dog", "Romeo", 8, "blue", "Male", "Yorkie")
print(dog.get_name())
print(dog.get_breed())

dog = Animal("Dog", "Romeo", 8, "blue", "Male")
print(dog.get_breed()) # will error