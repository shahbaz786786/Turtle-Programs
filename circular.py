import turtle
c=turtle.Turtle()
c.speed(100)
c.pen()
c.goto(-100,-100)
c.pendown()
for i in range(300):
    c.circle(i)

turtle.done()