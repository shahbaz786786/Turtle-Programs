import turtle
c=turtle.Turtle()

c.color("red","lime")

c.begin_fill()
for i in range(20):
    c.forward(200)
    c.left(135)
c.end_fill()

turtle.done()