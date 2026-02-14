import turtle

screen = turtle.Screen()
screen.bgcolor("plum")

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

current_player = "X"

board = []
# 0 1 2
# 3 4 5
# 6 7 8

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
    
def draw_symbol(x, y, symbol):
    drawer.goto(x, y - 35)

    if symbol == "X":
        drawer.color("red")
        drawer.write("X", align="center", font=("Arial", 60, "bold"))
    else:
        drawer.color("black")
        drawer.write("O", align="center", font=("Arial", 60, "bold"))
    
def handle_click(square):
    global current_player, board
    
    if square["taken"]:
        return
        
    # draw X or O in the center
    draw_symbol(square["x"], square["y"], current_player)
    square["taken"] = True
    
    result = check_winner()
    
    if result:
        pass
        # need to complete this part
    
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

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
        
        # attach click handler
        button.onclick(lambda x, y, s=square: handle_click(s))

screen.mainloop()