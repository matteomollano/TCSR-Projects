import turtle

screen = turtle.Screen()
screen.bgcolor("plum")

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
        # need to implement button.onclick() next

screen.mainloop()