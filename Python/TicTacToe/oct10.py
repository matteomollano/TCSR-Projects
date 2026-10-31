import random

board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_position(board):
    while True:
        try:
            position = int(input("Choose position (1-9): "))
        except ValueError:
            print("You must enter a number only.")
            continue

        if position < 1 or position > 9:
            print("You must choose a value from 1-9.")
            continue

        if board[position - 1] != "-":
            print("That position is already taken. Choose another.")
            continue

        return position

def get_char():
    char = input("Would you like to be X or O? ").upper().strip()
    options = ("X", "O")
    while char not in options:
        char = input("You must enter X or O: ").upper().strip()
    return char

def get_cpu_position(board):
    open_spots = []
    for i in range(len(board)):
        if board[i] == "-":
            open_spots.append(i)
    return random.choice(open_spots)

def check_win(board, symbol):
    win_list = [
        [0, 1, 2], # rows
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6], # columns
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8], # diagonals
        [2, 4, 6]
    ]

    for win_condition in win_list:
        if board[win_condition[0]] == symbol \
            and board[win_condition[1]] == symbol \
            and board[win_condition[2]] == symbol:
                return True

    return False

def check_tie(board):
    return "-" not in board

def main():
    player = get_char()
    cpu = "O" if player == "X" else "X"

    while True:
        print_board(board)
        player_position = get_position(board)
        board[player_position - 1] = player
        if check_win(board, player):
            print_board(board)
            print("You win!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        cpu_position = get_cpu_position(board)
        board[cpu_position] = cpu
        if check_win(board, cpu):
            print_board(board)
            print("You lose. CPU wins")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break


if __name__ == "__main__":
    main()
