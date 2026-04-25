import random

EMOJIS = ["⚽️", "🐕", "🌎", "🚗", "🦊", "🍪"]
balance = 100

# display welcome screen
def show_welcome():
    print("=================================")
    print("|      Emoji Slot Machine       |")
    print("=================================")
    print("|  Match emojis to win coins!   |")
    print("|  2 of a kind  →  2x your bet  |")
    print("|  3 of a kind  →  10x your bet |")
    print("=================================")

# ask the player how much they want to bet
def get_bet(balance):
    print(f"Your balance is {balance}")
    while True:
        bet = input("How many coins do you want to bet? ")
        
        if not bet.isdigit():
            print("Please enter a number!\n")
        elif int(bet) > balance:
            print("You don't have enough coins!\n")
        elif int(bet) <= 0:
            print("Bet must be at least one coin!\n")
        else:
            return int(bet)

# get 3 random emojis
def spin():
    result = []
    for i in range(3):
        result.append(random.choice(EMOJIS))
    return result

# display the spin result
def display_spin(result):
    print("\n+------------+")
    print(f"| {result[0]}  {result[1]}  {result[2]} |")
    print("+------------+\n")
   
# determine the spin result and return the winnings
def check_win(result, bet):
    """
    - 3 of the same = jackpot (10x bet)
    - 2 of the same = small win (2x bet)
    - No match = lose bet
    """
    if result[0] == result[1] == result[2]:
        print("🎉 JACKPOT! Three of a kind!")
        return bet * 10
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        print("✨ Nice! Two of a kind!")
        return bet * 2
    else:
        print("😢 No match. Better luck next time!")
        return 0
    
# update and return the new balance
def update_balance(balance, bet, winnings):
    """Updates and returns the new balance."""
    balance = balance - bet + winnings
    return balance

# display the game over screen
def show_game_over(balance):
    print("\n==============================")
    print("          GAME OVER!          ")
    print("==============================")
    if balance > 100:
        print(f"Good job! You finished with {balance} coins!")
        print(f"You made a profit of {balance - 100} coins.")
    elif balance == 100:
        print(f"You broke even with {balance} coins. Not bad.")
    else:
        print(f"You finished with {balance} coins.")
        print(f"You lost {100 - balance} coins. Try again next time.")
        
# show welcome screen
show_welcome()

while balance > 0:
    # get player's bet
    bet = get_bet(balance)

    # spin to get 3 emojis
    result = spin()
        
    # display spin result
    display_spin(result)

    # check if they won
    winnings = check_win(result, bet)

    # update and display new balance
    balance = update_balance(balance, bet, winnings)

    if winnings > 0:
        print(f"You won {winnings} coins!")
    print(f"New balance: {balance} coins\n")

    # ask if they want to keep playing
    if balance > 0:
        again = input("Spin again? (yes/no): ").strip().lower()
        if again != "yes" and again != "y":
            break

    print()

# display game over screen
show_game_over(balance)