import turtle
from math import sqrt # for accurate dimensions
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Start position
my_turtle.penup()
my_turtle.goto(-400, 200)
my_turtle.pendown()

# Dark blue rectangle
my_turtle.color("dark blue")
my_turtle.begin_fill()
my_turtle.fd(800)
my_turtle.rt(90)
my_turtle.fd(80)
my_turtle.rt(90)
my_turtle.fd(800)
my_turtle.rt(180)
my_turtle.end_fill()

# White stripe
my_turtle.color("white")
my_turtle.begin_fill()
my_turtle.fd(800)
my_turtle.rt(90)
my_turtle.fd(80)
my_turtle.rt(90)
my_turtle.fd(800)
my_turtle.rt(180)
my_turtle.end_fill()

# Dark blue rectangle
my_turtle.color("dark blue")
my_turtle.begin_fill()
my_turtle.fd(800)
my_turtle.rt(90)
my_turtle.fd(80)
my_turtle.rt(90)
my_turtle.fd(800)
my_turtle.rt(180)
my_turtle.end_fill()

# White stripe
my_turtle.color("white")
my_turtle.begin_fill()
my_turtle.fd(800)
my_turtle.rt(90)
my_turtle.fd(80)
my_turtle.rt(90)
my_turtle.fd(800)
my_turtle.rt(180)
my_turtle.end_fill()

# Dark blue rectangle
my_turtle.color("dark blue")
my_turtle.begin_fill()
my_turtle.fd(800)
my_turtle.rt(90)
my_turtle.fd(80)
my_turtle.rt(90)
my_turtle.fd(800)
my_turtle.rt(180)
my_turtle.end_fill()

# Red triangle
my_turtle.color("red")
my_turtle.begin_fill()
my_turtle.goto(-400 + sqrt(120000), 0)
my_turtle.lt(330)
my_turtle.fd(-400)
my_turtle.end_fill()

# White star
my_turtle.penup()
my_turtle.setheading(0)
my_turtle.goto(-250, 10)
my_turtle.pendown()
my_turtle.color("white")
my_turtle.begin_fill()
for i in range(5):
    my_turtle.fd(-90)
    my_turtle.lt(144)
my_turtle.end_fill()
my_turtle.hideturtle()

turtle.done()