from Hand import Hand

class Player:
    
    # name
    # uses Hand object
    # balance
    
    def __init__(self, name):
        self.name = name
        self.hand = Hand(2)  # start with 2 cards
        self.balance = 5000.00
        self.has_hit = False
        self.has_doubled = False

    def add_card(self):
        self.hand.add_card()

    def display_hand(self):
        print(f"{self.name}'s hand:")
        self.hand.display_hand()
        print(f"Total: {self.hand.get_total()}\n")

    def get_total(self):
        return self.hand.get_total()
    
    def get_balance(self):
        return self.balance
    
    def set_balance(self, new_balance):
        self.balance = new_balance
    
    def troll_balance(self, bet_amount):
        if self.balance < 1000:
            self.balance -= bet_amount * 0.07
            print("We don't not like poor people in Las Vegas. Your bet has been reduced by a 7% extreme poverty fee.")
        elif self.balance < 50000:
            self.balance -= bet_amount * 0.05
            print("We don't not like poor people in Las Vegas. You bet has been reduced by a 5% extreme poverty fee.")
        print(f"Your updated balance: {self.balance}")
            
    def add_balance(self, value):
        self.balance += value
        
    def sub_balance(self, value):
        self.balance -= value
        
    def update_hit(self):
        self.has_hit = True
        
    def get_hit(self):
        return self.has_hit
    
    def update_doubled(self):
        self.has_doubled = True
        
    def get_doubled(self):
        return self.has_doubled
    
    def busted(self):
        return self.get_total() > 21

    def reset_hand(self):
        self.hand.reset_hand()
        self.has_hit = False
        self.has_doubled = False