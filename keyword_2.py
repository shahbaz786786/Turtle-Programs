import turtle
import math
c=turtle.Turtle()
c.speed(100)
for i in range(1000):
    c.forward(10)
    c.left(math.sin(i/10)*25)
    c.left(20)

turtle.done()