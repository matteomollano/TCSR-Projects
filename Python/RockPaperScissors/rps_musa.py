import random

def normal_ai():
    print("You chose Normal AI!")
    cpu = random.choice(["rock", "paper", "scissors"])
    answer = input("Choose rock, paper, or scissors! ")
    
    while answer not in ["rock", "paper", "scissors"]:
        answer = input("Enter rock, paper, or scissors as lowercase only: ")
        
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if cpu == answer:
        print(f"You tied. You both chose {cpu}")
        return False
    else:
        if win_conditions[answer] == cpu:
            print(f"You win. Computer chose {cpu}")
            return True
        else:
            print(f"You lose. Computer chose {cpu}")
            return False
    
def super_ai():
    print("You chose Super AI")
    while True:
        answer = input("Choose rock, paper, or scissors! ")
        if answer == "rock":
            print("You lose. Computer chose paper")
        elif answer == "paper":
            print("You lose. Computer chose scissors")
        elif answer == "scissors":
            print("You lose. Computer chose rock")
        else:
            print("Invalid input. Enter rock, paper, or scissors as lowercase.")
        print()

beat_normal = False

while True:
    choice = int(input("Choose between Normal AI or Super AI! 1 for AI, 2 for Super AI: "))
    
    if choice == 2 and not beat_normal:
        print("You must beat Normal AI first!")
    elif choice == 2 and beat_normal:
        super_ai()
    elif choice == 1:
        did_win = normal_ai()
        if did_win:
            beat_normal = True
    else:
        print("Enter 1 or 2 only.")
    print()