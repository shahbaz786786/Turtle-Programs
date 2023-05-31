import turtle
import random
c=turtle.Turtle()
c.speed(10)
colors=['cyan','magenta','lime','black','red','yellow']
for i in range(100):
    c.color(random.choice(colors))
    c.forward(i*3)
    c.left(120)

turtle.done()