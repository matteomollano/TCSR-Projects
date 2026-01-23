from Dealer import Dealer
from Player import Player
import math

def get_two_decimal_number(decimal_places=2):
    while True:
        user_input = input("Please enter your bet amount: ")
        try:
            number = float(user_input)
            
            # Calculate the rounding factor (10^decimal_places)
            factor = 10 ** decimal_places
            
            # Multiply by the factor, floor it, then divide by the factor to round down
            rounded_number = math.floor(number * factor) / factor
            
            return abs(rounded_number)
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

# ask for the player's bet
def get_bet():
    while True:
        try:
            # bet_amount = float(input("Please state the amount of your bet: "))
            bet_amount = get_two_decimal_number()
            if bet_amount <= player.get_balance():
                return bet_amount
            else:
                print("Your bet amount exceeds your balance, and a 10% overdraft fee has been applied to your balance.")
                overdraft_fee = player.get_balance() * 0.10
                overdraft_fee = round(overdraft_fee, 2)
                print("overdraft fee:", overdraft_fee)
                player.sub_balance(overdraft_fee)
                print(f"Your new balance after overdraft fee is {player.get_balance()}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# handles the logic for doubling the bet
def process_doubled_bet(bet_amount):
    player_balance = player.get_balance()
    if bet_amount <= player_balance:
        player.sub_balance(bet_amount)
        player.add_card()
        player.update_doubled()
        return True
    else:
        print("Your doubled bet amount is too high. A 14% overdraft charge has been subtracted from your account.")
        player.sub_balance(0.14 * player_balance)
        return False

# update the player's balance when they win a bet       
def apply_winnings(bet_amount):
    if player.get_doubled():
        player.add_balance(bet_amount * 4)
    else:
        player.add_balance(bet_amount * 2)
   
# ask the user if they want to play again     
def play_again():
    play_again = input("\nDo you want to bet again? (Y/n): ").strip().upper()
    while play_again not in ['', 'Y', 'N']:
        play_again = input("Not a valid option. Please enter Y or N: ").strip().upper()
    return play_again

# play a single round
def play_round():
    print("Your balance is", player.get_balance())
    bet_amount = get_bet()
    player.sub_balance(bet_amount)
    print("Your updated balance is", player.get_balance(), "\n")

    # troll the player's balance
    # player.troll_balance(bet_amount)

    while True:
        if player.busted():
            player.display_hand()
            dealer.display_hand(hide_first_card=False)
            
            print("You have busted. A 5% dealer inconvenience fee has been billed to your account.")
            print("Dealer wins!")
            inconvenience_fee = round(0.05 * player.get_balance(), 2)
            player.sub_balance(inconvenience_fee)
            break
        else:
            player.display_hand()
            dealer.display_hand()
        
        if player.get_hit():
            options = "S for Stand, H for Hit"
            valid_choices = "S or H"
        else:
            options = "S for Stand, H for Hit, D for Double"
            valid_choices = "S, H, or D"
        
        option = input(f"Select an option ({options}): ").upper()
        
        if option == "S":
            break  # you chose to stand so end turn here
        elif option == "H":
            player.add_card()
            player.update_hit()
        elif option == "D" and not player.get_hit():
            if process_doubled_bet(bet_amount):
                break
        else:
            print(f"Invalid option. You must enter {valid_choices}.")
            
    # outside while loop do dealer's logic
    if not player.busted():
    
        while dealer.get_total() < 17:
            dealer.add_card()
        player.display_hand()
        dealer.display_hand(hide_first_card=False)
    
        if dealer.busted():
            print("Dealer busted. You win!")
            apply_winnings(bet_amount)
            
        else: 
            if dealer.get_total() > player.get_total():
                print("Dealer wins!")
                
            elif dealer.get_total() < player.get_total():
                print("You win!")
                apply_winnings(bet_amount)
                
            else: # equal
                print("It's a draw. A push has been applied and your bet has been returned.")
                if player.get_doubled():
                    player.add_balance(bet_amount * 2)
                else:
                    player.add_balance(bet_amount)
                

    print("Your total was", player.get_total())
    print("Dealer's total was", dealer.get_total())
    print("Your updated balance is", player.get_balance())
    
# run game here
print("Welcome to Blackjack!")
dealer = Dealer()
player = Player(name="Harnaik")

def main():
    round_number = 1
    while True:
        print(f"\n---------- Bet Number {round_number} ----------")
        play_round()
        
        if player.get_balance() == 0:
            print("You have no money left. You are kicked out of the casino!")
            break
            
        if play_again() == 'N':
            break
        else:
            round_number += 1
            player.reset_hand()
            dealer.reset_hand()
            
main()