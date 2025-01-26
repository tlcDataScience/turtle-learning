import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(1200, 700)

# Set the screen background
screen.bgpic("maze6.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-232.5, 330)
my_turtle.setheading(-90)
my_turtle.pendown()
my_turtle.pencolor("red")

my_turtle.fd(60)
my_turtle.lt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(50)
my_turtle.lt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.lt(90)
my_turtle.fd(250)
my_turtle.lt(90)
my_turtle.fd(200)
my_turtle.rt(90)
my_turtle.fd(50)

turtle.done()