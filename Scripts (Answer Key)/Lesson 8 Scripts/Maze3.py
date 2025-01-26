import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(1200, 700)

# Set the screen background
screen.bgpic("maze3.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-250, 255)
my_turtle.pendown()
my_turtle.pencolor("red")

my_turtle.fd(75)
my_turtle.rt(90)
my_turtle.fd(60)
my_turtle.lt(90)
my_turtle.fd(240)
my_turtle.rt(90)
my_turtle.fd(120)
my_turtle.rt(90)
my_turtle.fd(180)
my_turtle.lt(90)
my_turtle.fd(180)
my_turtle.lt(90)
my_turtle.fd(58)
my_turtle.rt(90)
my_turtle.fd(125)

turtle.done()