import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(1200, 700)

# Set the screen background
screen.bgpic("maze8.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-130, 330)
my_turtle.setheading(-90)
my_turtle.pendown()
my_turtle.pencolor("red")

my_turtle.fd(33)
my_turtle.lt(30)
my_turtle.fd(30)
my_turtle.lt(60)
my_turtle.fd(60)
my_turtle.rt(60)
my_turtle.fd(90)
my_turtle.rt(60)
my_turtle.fd(30)
my_turtle.rt(60)
my_turtle.fd(60)
my_turtle.lt(60)
my_turtle.fd(85)
my_turtle.lt(60)
my_turtle.fd(80)
my_turtle.lt(60)
my_turtle.fd(60)
my_turtle.rt(60)
my_turtle.fd(30)
my_turtle.rt(60)
my_turtle.fd(90)
my_turtle.rt(60)
my_turtle.fd(60)
my_turtle.lt(60)
my_turtle.fd(30)
my_turtle.lt(60)
my_turtle.fd(120)
my_turtle.rt(30)
my_turtle.fd(20)

turtle.done()