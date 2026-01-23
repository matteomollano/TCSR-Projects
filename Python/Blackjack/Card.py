import random

class Card:
    
    # suit
    # number
    
    def __init__(self):
        self.suit = self.get_random_suit()
        self.number = self.get_random_number()
        
    @staticmethod
    def get_random_suit():
        suits = ["♠️", "❤️", "♦", "♣"]
        suit = random.choice(suits)
        return suit
    
    @staticmethod
    def get_random_number():
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        number = random.choice(numbers)
        return number
    
    def get_suit(self):
        return self.suit
    
    def get_number(self):
        return self.number
    
    def display_card(self):
        print(f"{self.suit}  {self.number}")