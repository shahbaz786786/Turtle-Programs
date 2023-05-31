import turtle
import math
c=turtle.Turtle()

c.color("red","lime")
c.speed(100)  #ye cursor ki speed ko increase krta ha
c.begin_fill()
for i in range(100):
    c.forward(math.sqrt(i)*10)  # Math library ka use huwa ha
    c.left(i%100)
c.end_fill()

turtle.done()