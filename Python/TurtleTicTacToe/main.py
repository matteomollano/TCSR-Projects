import turtle

screen = turtle.Screen()
screen.bgcolor("plum")

current_player = "X"
game_over = False

board = [None] * 9 # stores X, O, or None
squares = [] # stores info about each square

# used for drawing X and O
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

# used for displaying current player
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-300, 270)
writer.write(f"Player 1's turn: {current_player}", font=("Arial", 20, "bold"))

# restart button
restart_button = turtle.Turtle()
restart_button.hideturtle()
restart_button.penup()
restart_button.speed(0)
restart_button.goto(250, 270)  # top right
restart_button.shape("square")
restart_button.color("lightgray")
restart_button.turtlesize(2, 5)

# --- function to draw X or O ---
def draw_symbol(x, y, symbol):
    drawer.goto(x, y - 35)

    if symbol == "X":
        drawer.color("red")
        drawer.write("X", align="center", font=("Arial", 60, "bold"))
    else:
        drawer.color("black")
        drawer.write("O", align="center", font=("Arial", 60, "bold"))

# --- function to check for a winner ---
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # vertical
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != None:
            return "Win"
    
    if None not in board:
        return "Draw"

    return None

# --- function to restart game ---
def restart_game(x=None, y=None):
    global current_player, game_over

    # reset game state
    current_player = "X"
    game_over = False

    # clear drawings and text
    drawer.clear()
    writer.clear()

    writer.write(f"Player 1's turn: {current_player}", font=("Arial", 20, "bold"))

    # reset board data
    for i, square in enumerate(squares):
        square["taken"] = False
        board[i] = None

    # hide restart button
    restart_button.clear()
    restart_button.hideturtle()
   
# --- click handler ---
def handle_click(square):
    global current_player, game_over
    
    # if square is already taken or game is over, do nothing
    if square["taken"] or game_over:
        return
        
    # draw X or O in the center
    draw_symbol(square["x"], square["y"], current_player)
    square["taken"] = True
    
    index = squares.index(square)
    board[index] = current_player
    
    result = check_winner()
    
    if result: # either Win or Draw
        game_over = True
        writer.clear()
        
        if result == "Win":
            writer.write(f"{current_player} wins!", font=("Arial", 20, "bold"))
        else:
            writer.write(f"Draw", font=("Arial", 20, "bold"))
        
        # show restart button
        restart_button.showturtle()
        restart_button.onclick(restart_game)
        
        return
      
    # switch players      
    if current_player == "X":
        current_player = "O"
        writer.clear()
        writer.write(f"Player 2's turn: {current_player}", font=("Arial", 20, "bold"))
    else:
        current_player = "X"
        writer.clear()
        writer.write(f"Player 1's turn: {current_player}", font=("Arial", 20, "bold"))

# create the board
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
        squares.append(square)
        
        # attach click handler
        button.onclick(lambda x, y, s=square: handle_click(s))

screen.mainloop()