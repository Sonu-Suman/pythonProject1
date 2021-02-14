import turtle
import random

colors = ["red", 'Orange', 'green', 'blue', 'pink', 'yellow', 'gray', 'white']
turtle.bgcolor("Black")
turtle.speed(10)

t = turtle.Turtle()

for x in range(100):
    t.pencolor(random.choice(colors))
    t.width(x//5 + 1)
    t.forward(x)
    t.left(20)

turtle.done()