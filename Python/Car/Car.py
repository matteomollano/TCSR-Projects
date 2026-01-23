
class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
    
    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make
        
    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
    
    def __str__(self):
        return f"This car is a {self.color} {self.make} {self.model} from {self.year}"
    
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', '{self.color}', '{self.year}')"
    
if __name__ == "__main__":
    car1 = Car("Chevrolet", "Corvette", "Blue", 2023)