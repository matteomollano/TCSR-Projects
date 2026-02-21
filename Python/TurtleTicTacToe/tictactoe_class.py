import turtle

screen = turtle.Screen()
screen.bgcolor("plum")

current_player = "X"
game_over = False

# keep track of each square's state
squares = []

# board is empty originally
board = [None] * 9
# Indices:
# 0 1 2
# 3 4 5
# 6 7 8

# used for drawing X and O
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

# used to display current player
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)
writer.goto(-300, 270)
writer.write(f"Player 1's turn: {current_player}", font=("Arial", 20, "bold"))

# function to check for game winner
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
        [0, 4, 8], [2, 4, 6] # diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != None:
            return "Win"
    
    if None not in board:
        return "Draw"

    return None
   
# function to draw X or O in square 
def draw_symbol(x, y, symbol):
    drawer.goto(x, y - 35)

    if symbol == "X":
        drawer.color("red")
        drawer.write("X", align="center", font=("Arial", 60, "bold"))
    else:
        drawer.color("black")
        drawer.write("O", align="center", font=("Arial", 60, "bold"))

# function that runs when a square is clicked
def handle_click(square):
    global current_player, game_over
    
    # if square is already taken
    # if game is over
    # don't do anything (return)
    if square["taken"] or game_over:
        return
        
    # draw X or O in the center
    draw_symbol(square["x"], square["y"], current_player)
    square["taken"] = True
    
    # put current player symbol (X or O) into list position that matches board spot
    index = squares.index(square)
    board[index] = current_player
    
    result = check_winner()
    
    if result:
        game_over = True
        writer.clear()
        
        if result == "Win":
            writer.write(f"{current_player} wins!", font=("Arial", 20, "bold"))
        else: # draw
            writer.write("It's a draw!", font=("Arial", 20, "bold"))

        return
    
    # switch turn
    writer.clear()
    if current_player == "X":
        current_player = "O"
        writer.write(f"Player 2's turn: {current_player}", font=("Arial", 20, "bold"))
    else:
        current_player = "X"
        writer.write(f"Player 1's turn: {current_player}", font=("Arial", 20, "bold"))

# board creation
for row in [150, 0, -150]: # row
    for col in [-150, 0, 150]: # column
        button = turtle.Turtle()
        button.shape("square")
        button.color("white")
        button.turtlesize(5, 5, 5)
        button.penup()
        button.speed(0) 
        button.goto(col, row)

        # store square info
        square = {
            "turtle": button,
            "x": col,
            "y": row,
            "taken": False
        }
        # append to squares list
        squares.append(square)
        
        # attach click handler
        button.onclick(lambda x, y, s=square: handle_click(s))

screen.mainloop()