import turtle

c=turtle.Turtle()
# c.goto(15,8)
# c.backward(15)
# for i in range(100):
#     c.forward(1)
#     c.right(1)
c.penup()
c.goto(-200,100)
c.pendown()

c.rt(15)
c.forward(50)
c.backward(50)

c.lt(15)
c.forward(50)
c.left(50)
c.forward(40)


for i in range(130):
    c.rt(1)
    c.fd(1)

c.right(330)
c.forward(200)
c.setx(-100)

# for i in range(100):
#     c.left(1)
#     c.forward(1)


turtle.done()