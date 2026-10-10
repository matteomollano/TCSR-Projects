board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_position():
    position = input("Choose position (1-9): ")
    try:
        position = int(position)
        if position < 1 or position > 9:
            print("You must choose a value from 1-9")
    except ValueError:
        print("You must enter a number only")
