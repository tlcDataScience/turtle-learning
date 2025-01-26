import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(1200, 700)

# Set the screen background
screen.bgpic("maze7.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-430, 280)
my_turtle.setheading(-90)
my_turtle.pendown()
my_turtle.pencolor("red")

my_turtle.fd(180)
my_turtle.rt(60)
my_turtle.fd(70)
my_turtle.setheading(270)
my_turtle.fd(80)
my_turtle.lt(120)
my_turtle.fd(70)
my_turtle.rt(60)
my_turtle.fd(70)
my_turtle.lt(60)
my_turtle.fd(70)
my_turtle.rt(120)
my_turtle.fd(80)
my_turtle.lt(60)
my_turtle.fd(140)
my_turtle.lt(60)
my_turtle.fd(70)
my_turtle.rt(60)
my_turtle.fd(80)
my_turtle.rt(60)
my_turtle.fd(80)

turtle.done()