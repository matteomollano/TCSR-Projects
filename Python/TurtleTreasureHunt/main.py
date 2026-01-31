import turtle
import random

# --------------------
# Screen setup
# --------------------
screen = turtle.Screen()
screen.title("Turtle Treasure Hunt")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# --------------------
# Player turtle
# --------------------
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# --------------------
# Treasure turtle
# --------------------
treasure = turtle.Turtle()
treasure.shape("circle")
treasure.color("gold")
treasure.penup()
treasure.speed(0)
treasure.goto(random.randint(-250, 250), random.randint(-250, 250))

# --------------------
# Score display
# --------------------
score = 0
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)
score_writer.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# --------------------
# Movement functions
# --------------------
# Directions:
# 0   -> right
# 90  -> up
# 180 -> left
# 270 -> down
# --------------------
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# --------------------
# Keyboard bindings
# --------------------
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# --------------------
# Collision check
# --------------------
def check_collision(t1, t2):
    return t1.distance(t2) < 20

# --------------------
# Update Treasure
# --------------------
def update_treasure(t: turtle):
    shapes = ["circle", "square"]
    colors = ["gold", "DeepPink", "CornflowerBlue", "BlueViolet", "magenta", "DarkGreen"]
    t.shape(random.choice(shapes))
    t.color(random.choice(colors))
    t.goto(random.randint(-250, 250), random.randint(-250, 250))

# --------------------
# Main game loop
# --------------------
while True:
    screen.update()

    if check_collision(player, treasure):
        update_treasure(treasure)
        score += 1
        score_writer.clear()
        score_writer.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))