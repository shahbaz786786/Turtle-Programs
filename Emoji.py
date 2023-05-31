#importing turtle module
import turtle

# turtle object
smiley = turtle.Turtle()



# function for creation of eye
def eye(col, rad):
	smiley.down()
	smiley.fillcolor(col)
	smiley.begin_fill()
	smiley.circle(rad)
	smiley.end_fill()
	smiley.up()


# draw face
smiley.width(4)
smiley.fillcolor('yellow')
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()
smiley.up()

# draw eyes
smiley.goto(-40, 120)
eye('white', 15)
smiley.goto(-37, 130)
eye('black', 5)
smiley.goto(40, 120)
eye('white', 15)
smiley.goto(37, 130)
eye('black', 5)

# draw mouth
smiley.goto(-40, 85)
smiley.down()
smiley.right(90)
smiley.circle(40, 180)
smiley.up()

# draw tongue
smiley.goto(-10, 45)
smiley.down()
smiley.right(180)
smiley.fillcolor('red')
smiley.begin_fill()
smiley.circle(10, 180)
smiley.end_fill()
smiley.hideturtle()