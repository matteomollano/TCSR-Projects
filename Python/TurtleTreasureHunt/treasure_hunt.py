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

screen.mainloop()