import turtle
import math
c=turtle.Turtle()

c.color("red","lime")
c.speed(1000)  #ye cursor ki speed ko increase krta ha

for i in range(1000):
    c.forward(math.sqrt(i))  # Math library ka use huwa ha
    c.left(i%180)


turtle.done()