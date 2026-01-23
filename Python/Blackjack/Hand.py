from Card import Card

class Hand:
    
    # hand (list of cards)
    # total
    
    def __init__(self, num_of_cards):
        self.hand = []
        self.total = 0
        
        # initialize hand
        for i in range(num_of_cards):
            new_card = Card()
            self.hand.append(new_card)
        
        # initialize total
        for card in self.hand:
            number = card.get_number()
            self.update_total(number)
            
    def update_total(self, card_value):
        if card_value in ["2","3","4","5","6","7","8","9","10"]:
            self.total += int(card_value)
        elif card_value in ["J", "Q", "K"]:
            self.total += 10
        else: # A
            check_over_21 = self.total + 11
            if check_over_21 > 21:
                self.total += 1
            else:
                self.total += 11
                
    def display_hand(self):
        for card in self.hand:
            card.display_card()

    def add_card(self):
        # add a new random card to self.hand
        new_card = Card()
        self.hand.append(new_card) 
        
        # add the new card's value to the total
        number = new_card.get_number()
        self.update_total(number)
        
    def get_hand(self):
        return self.hand
            
    def get_total(self):
        return self.total
    
    def reset_hand(self):
        self.hand.clear()
        self.total = 0
        
        for i in range(2):
            new_card = Card()
            self.hand.append(new_card)
        
        # initialize total
        for card in self.hand:
            number = card.get_number()
            self.update_total(number)