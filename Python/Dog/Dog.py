class Dog: 
    
    def __init__(self, name, breed, age, gender):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\nGender: {self.gender}"
