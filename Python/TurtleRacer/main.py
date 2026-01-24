import turtle
import random

screen = turtle.Screen()
colors = ["red", "blue", "green", "orange", "purple"]
racers = []

for i in range(len(colors)):
    t = turtle.Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-200, 100 - i*40)
    racers.append(t)

for turn in range(100):
    for r in racers:
        r.forward(random.randint(1, 10))

screen.exitonclick()