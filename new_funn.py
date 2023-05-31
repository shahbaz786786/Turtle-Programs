import turtle

c=turtle.Turtle()
c.getscreen()                #c.getscreen().bgcolor()
c.screen.bgcolor("#994444")

def star(turtle,size):
    if size<=10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/2)
            turtle.left(216)
star(c,100)
turtle.done()