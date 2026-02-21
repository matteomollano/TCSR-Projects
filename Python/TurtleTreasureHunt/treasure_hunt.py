import turtle
import random

screen = turtle.Screen()
screen.bgcolor("teal")

tortoise = turtle.Turtle()
tortoise.shape("turtle")
tortoise.speed(0)
tortoise.penup()

treasure = turtle.Turtle()
treasure.shape("circle")
treasure.color("gold")
treasure.penup()
treasure.speed(0)
treasure.goto(random.randint(-250, 250), random.randint(-250, 250))

score = 0
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)
writer.goto(0, 280)
writer.write("Score: 0", align="center", font=("Arial", 30, "bold"))

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

# screen.mainloop()

while True:
    screen.update()
    
    # for debugging
    # print(tortoise.distance(treasure))

    # tortoise collects treasure
    if tortoise.distance(treasure) <= 22:
        # want to move the treasure
        treasure.goto(random.randint(-250, 250), random.randint(-250, 250))
        
        # randomize its color
        colors = ["lightpink", "lightblue", "magenta", "lightgreen"]
        treasure.color(random.choice(colors))
        
        # randomize shape
        shapes = ["turtle", "circle", "square", "triangle"]
        treasure.shape(random.choice(shapes))
        
        # update score
        score = score + 1
        writer.clear()
        writer.write(score, align="center", font=("Arial", 30, "bold"))