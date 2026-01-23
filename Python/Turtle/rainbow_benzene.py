import turtle

t = turtle.Pen()
window = turtle.Screen()
window.bgcolor('black')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

for i in range(240):
    t.pencolor(colors[i%6])
    #t.width(i//100 + 1)
    t.forward(i)
    t.left(59)
    
turtle.done()