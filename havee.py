import turtle
import random
c=turtle.Turtle()
c.speed(10)
co=['blue','black','lime','cyan','pink','red','green']

for i in range(50):
    c.color(random.choice(co))
    c.circle(i)



turtle.done()