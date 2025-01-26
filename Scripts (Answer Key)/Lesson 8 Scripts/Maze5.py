import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(1200, 700)

# Set the screen background
screen.bgpic("maze5.png")

my_turtle.showturtle()
my_turtle.shape("turtle")

# Bring the turtle to the starting point
my_turtle.penup()
my_turtle.goto(-190, 240)
my_turtle.pendown()
my_turtle.pencolor("red")

my_turtle.fd(200)
my_turtle.rt(90)
my_turtle.fd(100)
my_turtle.rt(90)
my_turtle.fd(70)
my_turtle.lt(90)
my_turtle.fd(60)
my_turtle.lt(90)
my_turtle.fd(60)
my_turtle.rt(90)
my_turtle.fd(60)
my_turtle.rt(90)
my_turtle.fd(120)
my_turtle.lt(90)
my_turtle.fd(190)
my_turtle.lt(60)
my_turtle.fd(72)
my_turtle.setheading(270)
my_turtle.fd(35)

turtle.done()