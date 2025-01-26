import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(1200, 700)

# Set the screen background
screen.bgpic("maze4.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-280, 211)
my_turtle.pendown()
my_turtle.pencolor("red")

my_turtle.fd(350)
my_turtle.rt(90)
my_turtle.fd(120)
my_turtle.rt(52)
my_turtle.fd(210)
my_turtle.rt(75)
my_turtle.fd(110)
my_turtle.setheading(270)
my_turtle.fd(120)
my_turtle.lt(50)
my_turtle.fd(110)
my_turtle.setheading(270)
my_turtle.fd(70)

turtle.done()