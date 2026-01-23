from Hand import Hand

class Dealer:
    
    # uses Hand object
    
    def __init__(self):
        self.hand = Hand(2)  # start with 2 cards

    def add_card(self):
        self.hand.add_card()

    def display_hand(self, hide_first_card=True):
        print("Dealer's Hand:")
        if hide_first_card:
            print("Hidden Card")
            self.hand.get_hand()[1].display_card()  # show only the second card
            print()
        else:
            self.hand.display_hand()
            print(f"Total: {self.get_total()}\n")

    def get_total(self):
        return self.hand.get_total()
    
    def busted(self):
        return self.get_total() > 21
    
    def reset_hand(self):
        self.hand.reset_hand()