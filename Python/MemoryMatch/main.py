import random, os, time

emojis = ['🍎', '😂', '🐶', '🦊', '🦋', '🐻', '🥝', '🦈']
emoji_pairs = emojis * 2
random.shuffle(emoji_pairs)

# ['🍎', '😂', '🐶', '🦊', '🦋', '🐻', '🥝', '🦈', '🍎', '😂', '🐶', '🦊', '🦋', '🐻', '🥝', '🦈']

# [
#     ['🍎', '😂', '🐶', '🦊'],
#     ['🦋', '🐻', '🥝', '🦈'],
#     ['🍎', '😂', '🐶', '🦊'],
#     ['🦋', '🐻', '🥝', '🦈']
# ]

# create board
GRID_SIZE = 4
board = []
for i in range(GRID_SIZE):
    board.append(emoji_pairs[i * GRID_SIZE:(i + 1) * GRID_SIZE])
    
# keep track of which emojis were guessed correctly
visible = []
for i in range(GRID_SIZE):
    visible.append([False] * 4)

def print_board(board, visible):
    print("  1  2  3  4")
    for i in range(GRID_SIZE):
        row = []
        for j in range(GRID_SIZE):
            if visible[i][j]:
                row.append(board[i][j])
            else:
                row.append('❓')
        print(f"{i+1} " + ' '.join(row))

def get_input():
    while True:
        try:
            coordinates = input("Enter row and column (ex. 2 4): ")
            coordinates = coordinates.strip().split() # "2 4        " -> "2 4" -> ["2", "4"]
            if len(coordinates) != 2:
                raise ValueError
            x, y = int(coordinates[0]), int(coordinates[1])
            if (x < 1 or x > 4) or (y < 1 or y > 4):
                raise ValueError
            # passed all of the error checks
            if visible[x-1][y-1]:
                print("That emoji is already matched. Try another")
                continue
            return x-1, y-1
        except ValueError:
            print("Enter coordinates as two numbers (e.g., 0 1)")
            
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
   
def game_loop():
    matches_found = 0
    total_matches = len(emojis)
    
    while matches_found < total_matches:
        clear_screen()
        print_board(board, visible)
        
        print("Select the first emoji:")
        x1, y1 = get_input()
        visible[x1][y1] = True
        clear_screen()
        print_board(board, visible)
        
        print("Select the second emoji:")
        x2, y2 = get_input()
        visible[x2][y2] = True
        clear_screen()
        print_board(board, visible)
        
        if board[x1][y1] == board[x2][y2]:
            print("✅ It's a match!")
            time.sleep(1)
            matches_found += 1
        else:
            print("❌ Not a match.")
            time.sleep(2)
            # Reset the board for the mismatched emojis
            visible[x1][y1] = False
            visible[x2][y2] = False
            
    print("Congratulations! You matched all of the emoji pairs!")

if __name__ == "__main__":
    game_loop()