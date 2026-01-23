import random, time

board = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
]

# parameter
def print_board(board):
    print("  1", "  2", "  3")
    print("1", board[0][0],"|",board[0][1],"|",board[0][2])
    print("2", board[1][0],"|",board[1][1],"|",board[1][2])
    print("3", board[2][0],"|",board[2][1],"|",board[2][2])
    
def get_position(board):
    while True:
        try:
            position = input("Enter row,column (Ex: 1,2): ")
            x, y = position.split(",")
            x = int(x) - 1
            y = int(y) - 1

            if (0 <= x <= 2) and (0 <= y <= 2):
                return x, y
            else:
                print("Row and column must be between 1 and 3 only.")
        except ValueError:
            print("Invalid format. Please use row,column (e.g., 1,2).")

def check_win(board, symbol):
    # check rows
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True

    # check columns
    for i in range(3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True

    # check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# game start
player = input("Do you want to be X or O? ").upper()
while player not in ["X", "O"]:
    player = input("Only enter X or O: ").upper()

computer = ""
if player == "X":
    computer = "O"
else:
    computer = "X"
    
print_board(board)

while True:
    # player move
    row, col = get_position(board)

    while not board[row][col] == " ":
        print("The position is already taken.")
        row, col = get_position(board)
        
    # update board with player move
    board[row][col] = player
    print_board(board)
    
    # check if player won
    if check_win(board, player):
        print("Congratulations! You win!")
        break

    # check if tie
    if check_tie(board):
        print("It's a tie!")
    
    # computer move
    cpu_row = random.randint(0, 2)
    cpu_col = random.randint(0, 2)

    while not board[cpu_row][cpu_col] == " ":
        cpu_row = random.randint(0, 2)
        cpu_col = random.randint(0, 2)

    # update board with cpu move
    board[cpu_row][cpu_col] = computer
    print("\nComputer is choosing...")
    time.sleep(1)
    print_board(board)
    
    if check_win(board, computer):
        print("Computer wins. Better luck next time!")
        break

    if check_tie(board):
        print("It's a tie!")
        break