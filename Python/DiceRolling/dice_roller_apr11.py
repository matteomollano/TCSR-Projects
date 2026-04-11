import random, time

cpu_score = 0
player_score = 0

print("Welcome to dice roller. First to three wins!")
time.sleep(2)
print()

i = 1
while True:
    print(f"Round {i}")
    i += 1
    cpu = random.randint(1, 6)
    player = random.randint(1, 6)

    print("CPU is rolling...")
    time.sleep(2)
    print(f"CPU rolled a {cpu}")
    
    print("You are rolling...")
    time.sleep(2)
    print(f"You rolled a {player}")

    if cpu > player:
        cpu_score += 1
    elif player > cpu:
        player_score += 1
    else:
        print("Tie")
    
    print("Scoring...")
    time.sleep(2)
    print(f"Your score: {player_score}")
    print(f"CPU score: {cpu_score}")
        
    if cpu_score == 3:
        print("\nComputer wins")
        break
    
    if player_score == 3:
        print("\nYou win!")
        break
    
    print()