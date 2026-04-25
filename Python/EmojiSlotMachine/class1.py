import random

def show_welcome():
    print("=" * 34)
    print("|" + " " * 7 + "Emoji Slot Machine" + " " * 7 + "|")
    print("=" * 34)
    print("|" + "   Match emojis to win coins!   " + "|")
    print("|  2 of a kind  ->  2x your bet  |")
    print("|  3 of a kind  ->  10x your bet |")
    print("=" * 34)

def spin():
    emojis = ["⚽️", "🐕", "🌎", "🚗", "🦊", "🍪"]
    emoji_list = []
    for i in range(3):
        emoji_list.append(random.choice(emojis))
    return emoji_list

def display_spin(emoji_list):
    print("\n+------------+")
    print(f"| {emoji_list[0]}  {emoji_list[1]}  {emoji_list[2]} |")
    print("+------------+\n")
    
def get_bet(balance):
    print(f"You have {balance} coins.")
    
    while True:
        bet = input("How many coins do you want to bet? ")
        if bet.isalpha():
            print("You must enter a number.")
        elif int(bet) > balance:
            print("You don't have enough coins.")
        elif int(bet) <= 0:
            print("You must bet at least 1 coin.")
        else:
            break
    
    return int(bet)
        
    
    
balance = 100
show_welcome()

bet = get_bet(balance)

x = spin()
display_spin(x)