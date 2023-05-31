import turtle
c=turtle.Turtle()
c.speed(100)

c.penup()
c.goto(-200,50)
c.pendown()
c.left(20)
c.forward(60)
c.backward(60)
c.right(20)
c.forward(60)
c.backward(60)
c.left(20)
c.forward(60)

for i in range(60):
    c.forward(1)
    c.left(1)
c.setheading(60)
c.circle(-100,70)

for a in range(70):
    c.forward(1)
    c.right(1)

c.setheading(320)
c.forward(300)
c.setheading(190)
c.forward(320)
c.circle(-100,150)
c.forward(10)
c.seth(180)
c.forward(35)

c.pencolor("white")
c.seth(20)
c.forward(120)

c.pencolor("black")
c.circle(20)
c.setheading(90)
c.pencolor("white")
c.forward(20)

c.color('black','black')
c.begin_fill()
c.circle(10)
c.end_fill()

c.setheading(220)
c.pencolor("white")
c.forward(140)
c.setheading(10)
c.pencolor('black')
c.forward(259)
c.backward(259)
c.setheading(245)
c.forward(20)
c.setheading(10)
c.forward(279)

c.setheading(270)
c.circle(130,100)

# c.penup()
# c.goto(-150,70)
# c.pendown()
# c.forward(250)




turtle.done()