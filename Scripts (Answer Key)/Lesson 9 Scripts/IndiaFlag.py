import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Start position
my_turtle.penup()
my_turtle.goto(-400, 250)
my_turtle.pendown()

# Orange and white rectangles 
my_turtle.color("orange")
my_turtle.begin_fill()
my_turtle.forward(800)
my_turtle.right(90)
my_turtle.forward(167)
my_turtle.right(90)
my_turtle.forward(800)
my_turtle.end_fill()
my_turtle.left(90)
my_turtle.penup()
my_turtle.forward(167)

# Green rectangle
my_turtle.pendown()
my_turtle.color("green")
my_turtle.begin_fill()
my_turtle.forward(167)
my_turtle.left(90)
my_turtle.forward(800)
my_turtle.left(90)
my_turtle.forward(167)
my_turtle.end_fill()

# Big blue circle
my_turtle.penup()
my_turtle.goto(70, 0)
my_turtle.pendown()
my_turtle.color("navy")
my_turtle.begin_fill()
my_turtle.circle(70)
my_turtle.end_fill()

# Big white circle
my_turtle.penup()
my_turtle.goto(60, 0)
my_turtle.pendown()
my_turtle.color("white")
my_turtle.begin_fill()
my_turtle.circle(60)
my_turtle.end_fill()

# Mini blue circles
my_turtle.penup()
my_turtle.goto(-57, -8)
my_turtle.pendown()
my_turtle.color("navy")
for i in range(24):
	my_turtle.begin_fill()
	my_turtle.circle(3)
	my_turtle.end_fill()
	my_turtle.penup()
	my_turtle.forward(15)
	my_turtle.right(15)
	my_turtle.pendown()
	
# Small blue circle
my_turtle.penup()
my_turtle.goto(20, 0)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()

# Spokes
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()
my_turtle.pensize(2)
for i in range(24):
	my_turtle.forward(60)
	my_turtle.backward(60)
	my_turtle.left(15)

turtle.done()