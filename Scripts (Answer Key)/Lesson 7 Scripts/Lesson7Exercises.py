import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Exercise a
def draw_square():
    for i in range(4):
        my_turtle.fd(100)
        my_turtle.lt(90)

def draw_circle():
    my_turtle.circle(50)

def draw_triangle():
    for i in range(3):
        my_turtle.fd(100)
        my_turtle.lt(120)

# Exercise b
my_turtle.penup()
my_turtle.bk(200)
my_turtle.pendown()
draw_square()
my_turtle.penup()
my_turtle.fd(100)
my_turtle.fd(100)
my_turtle.pendown()
draw_circle()
my_turtle.penup()
my_turtle.fd(100)
my_turtle.pendown()
draw_triangle()

# Exercise c
def draw_hexagon(side_length, x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    for i in range(6):
        my_turtle.fd(side_length)
        my_turtle.lt(60)

draw_hexagon(150, 100, 0)

turtle.done()