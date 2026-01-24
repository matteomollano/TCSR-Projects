import turtle, random

screen = turtle.Screen()

# red, orange, yellow, green, blue, purple
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.penup()
turtle1.goto(-150, 175)

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("orange")
turtle2.penup()
turtle2.goto(-150, 125)

turtle3 = turtle.Turtle()
turtle3.shape("turtle")
turtle3.color("yellow")
turtle3.penup()
turtle3.goto(-150, 75)

turtle4 = turtle.Turtle()
turtle4.shape("turtle")
turtle4.color("green")
turtle4.penup()
turtle4.goto(-150, 25)

turtle5 = turtle.Turtle()
turtle5.shape("turtle")
turtle5.color("blue")
turtle5.penup()
turtle5.goto(-150, -25)

turtle6 = turtle.Turtle()
turtle6.shape("turtle")
turtle6.color("purple")
turtle6.penup()
turtle6.goto(-150, -75)

for i in range(100):
    turtle1.forward(random.randint(1, 10))
    turtle2.forward(random.randint(1, 10))
    turtle3.forward(random.randint(1, 10))
    turtle4.forward(random.randint(1, 10))
    turtle5.forward(random.randint(1, 10))
    turtle6.forward(random.randint(1, 10))

screen.exitonclick()