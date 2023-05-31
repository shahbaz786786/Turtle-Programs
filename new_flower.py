import turtle
c=turtle.Turtle()

c.color("red","yellow")
c.speed(10)  #ye cursor ki speed ko increase krta ha
c.begin_fill()
for i in range(100):
    c.forward(200)
    c.left(170)
c.end_fill()

turtle.done()