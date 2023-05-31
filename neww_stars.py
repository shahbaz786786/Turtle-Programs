import turtle

c=turtle.Turtle()
c.getscreen()                #c.getscreen().bgcolor()
c.screen.bgcolor("#994444")
c.penup()
c.goto(-200,100)
c.pendown()
c.speed(100)
def star(turtle,size):
    if size<=10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
star(c,360)
turtle.done()