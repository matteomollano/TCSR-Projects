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

def main():
    player = get_char()
    cpu = "O" if player == "X" else "X"

    while True:
        print_board(board)
        player_position = get_position(board)
        board[player_position - 1] = player

        cpu_position = get_cpu_position(board)
        board[cpu_position] = cpu

        # To-do: implement win and draw check

if __name__ == "__main__":
    main()
