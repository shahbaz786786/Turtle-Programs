import turtle
import math
c=turtle.Turtle()

c.color("red","lime")
c.speed(100)  #ye cursor ki speed ko increase krta ha

for i in range(1000):
    c.forward(100)
    c.left(math.sin(i/10)*25)  # Math library ka use huwa ha
    c.left(20)


turtle.done()