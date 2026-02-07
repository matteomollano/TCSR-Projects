import turtle
import random

screen = turtle.Screen()
screen.bgcolor("teal")

tortoise = turtle.Turtle()
tortoise.shape("turtle")
tortoise.penup()

treasure = turtle.Turtle()
treasure.shape("circle")
treasure.color("gold")
treasure.penup()
treasure.speed(0)
treasure.goto(random.randint(-250, 250), random.randint(-250, 250))

# 0 = right
# 90 = up
# 180 = left
# 270 = down

def right():
    tortoise.setheading(0)
    tortoise.forward(20)
    
def left():
    tortoise.setheading(180)
    tortoise.forward(20)

def up():
    tortoise.setheading(90)
    tortoise.forward(20)

def down():
    tortoise.setheading(270)
    tortoise.forward(20)

screen.listen()
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.mainloop()