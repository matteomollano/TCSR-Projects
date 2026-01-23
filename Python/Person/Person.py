# name, age, gender, height, hair color

class Person:
    # initialize
    def __init__(self, name, age, gender, height, hair_color):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.hair_color = hair_color
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Height: {self.height}")
        print(f"Hair Color: {self.hair_color}")
        
    def setName(self, new_name):
        self.name = new_name
    
    def getName(self):
        return self.name
    
    def setAge(self, new_age):
        self.age = new_age
    
    def getAge(self):
        return self.age
    
    def setGender(self, new_gender):
        self.gender = new_gender
    
    def getGender(self):
        return self.gender
    
    def setHeight(self, new_name):
        self.name = new_name
    
    def getHeight(self):
        return self.name
    
    def setHairColor(self, new_hair_color):
        self.hair_color = new_hair_color
        
    def getHairColor(self):
        return self.hair_color