import random
import os
import time

# Define emojis
emojis = ['🍎', '🍌', '🍇', '🍉', '🍓', '🍍', '🥝', '🍒']

# Duplicate and shuffle for pairs
emoji_pairs = emojis * 2
random.shuffle(emoji_pairs)

# Game settings
GRID_SIZE = 4
board = [emoji_pairs[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]
visible = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    print("   " + "  ".join(str(i) for i in range(GRID_SIZE)))
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            if visible[i][j]:
                row.append(board[i][j])
            else:
                row.append('❓')
        print(f"{i}  " + "  ".join(row))
    print()

def get_input(prompt):
    while True:
        try:
            coords = input(prompt).strip().split()
            if len(coords) != 2:
                raise ValueError
            x, y = map(int, coords)
            if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
                raise ValueError
            if visible[x][y]:
                print("That card is already matched or visible! Try another.")
                continue
            return x, y
        except ValueError:
            print("Enter coordinates as two numbers (e.g., 0 1).")

def game_loop():
    matches_found = 0
    total_matches = (GRID_SIZE * GRID_SIZE) // 2

    while matches_found < total_matches:
        clear_screen()
        print_board()

        print("Select the first card:")
        x1, y1 = get_input("Enter row and column: ")
        visible[x1][y1] = True
        clear_screen()
        print_board()

        print("Select the second card:")
        x2, y2 = get_input("Enter row and column: ")
        visible[x2][y2] = True
        clear_screen()
        print_board()

        if board[x1][y1] == board[x2][y2]:
            print("✅ It's a match!")
            matches_found += 1
        else:
            print("❌ Not a match.")
            time.sleep(2)
            visible[x1][y1] = False
            visible[x2][y2] = False

    print("🎉 Congratulations! You've matched all the pairs!")

if __name__ == '__main__':
    game_loop()