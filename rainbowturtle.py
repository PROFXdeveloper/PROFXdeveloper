import turtle
colors = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtle.bgcolor('black')
turtle.speed(0)
for x in range(200):
    turtle.pencolor(colors[x%7])
    turtle.width(x/100 + 1)
    turtle.forward(x)
    turtle.left(59)
turtle.done()
