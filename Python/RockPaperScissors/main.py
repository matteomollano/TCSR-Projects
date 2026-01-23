import random

choices = ['rock', 'paper', 'scissors']
win_conditions = {
    'rock':'scissors',
    'paper':'rock',
    'scissors':'paper'
}

round = 1
while True:
    print("Round", round)
    player = input('Choose rock, paper, or scissors: ').lower()
    while player not in choices:
        player = input('Invalid choice. Please enter rock, paper, or scissors only: ').lower()
    cpu = random.choice(choices)

    if player == cpu:
        print("Draw. You both played", player)
    else:
        if win_conditions[player] == cpu:
            print("Player wins with", player)
            print("CPU chose", cpu)
        else:
            print("CPU wins with", cpu)
            print("Player chose", player)
            
    play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again != 'y':
        break
    else:
        round += 1
        print()