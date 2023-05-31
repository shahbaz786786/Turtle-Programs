import turtle
import random
wn=turtle.Screen()
wn.bgcolor('cyan')
c=turtle.Turtle()
c.speed(0)
r=10
for i in range(100):
    c.circle(r+i,45)  # agr yaha pr '*' istmal krty han to zyada door door lines bany gi
    j=random.random()
    k=random.random()
    l=random.random()
    c.pencolor((l,j,k))
c.penup()
c.home()
c.pendown()

n=5
for i in range(100):
    c.circle(n+i,45)  # agr yaha pr '*' istmal krty han to zyada door door lines bany gi
    j=random.random()
    k=random.random()
    l=random.random()
    c.pencolor((l,j,k))
c.penup()
c.home()
c.pendown()

m=20
for i in range(100):
    c.circle(m+i,45)  # agr yaha pr '*' istmal krty han to zyada door door lines bany gi
    j=random.random()
    k=random.random()
    l=random.random()
    c.pencolor((l,j,k))
c.penup()
c.home()
c.pendown()





turtle.done()