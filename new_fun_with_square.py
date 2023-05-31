import turtle
c=turtle.Turtle()
c.color("blue","cyan")

c.begin_fill()

c.forward(100)
c.left(90)
c.forward(100)
c.left(90)
c.forward(100)
c.left(90)
c.forward(100)

c.penup()   # Ye wala space chorny k lye istmal hota ha
c.forward(50)  # Kitny pixels space chorni ha
c.pendown()  # Space ka ibtada ko end krny k lye

c.forward(100)    # 2sra square bnany k lye
c.left(90)
c.forward(100)
c.left(90)
c.forward(100)
c.left(90)
c.forward(100)

c.end_fill()  # agr begin_fill or end_fill 2nu table k 7 put kry gy to alag alag time pr color mily ga


turtle.done()