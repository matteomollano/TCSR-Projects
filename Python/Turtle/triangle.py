import turtle as t

t.begin_fill()
colors = ['blue', 'red', 'green']

for i in range(3):
    t.color(colors[i])
    t.forward(100)
    t.left(120)

t.fillcolor('lightblue')
t.end_fill()

t.mainloop()