import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Exercise a
my_turtle.shape("turtle")

# Exercise b
my_turtle.fd(25)

# Exercise c
my_turtle.penup()
my_turtle.fd(10)
my_turtle.pendown()
my_turtle.fd(50)

# Exercise d
my_turtle.left(90)
my_turtle.fd(100)

my_turtle.right(90)
my_turtle.penup()
my_turtle.fd(10)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.bk(100)

my_turtle.right(90)
my_turtle.penup()
my_turtle.fd(10)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.fd(100)

my_turtle.right(90)
my_turtle.penup()
my_turtle.fd(10)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.bk(100)

my_turtle.right(90)
my_turtle.penup()
my_turtle.fd(10)
my_turtle.pendown()
my_turtle.left(90)
my_turtle.fd(100)

# Exercise e
my_turtle.left(22.5)
my_turtle.fd(20)
my_turtle.left(135)
my_turtle.fd(20)
my_turtle.right(135)
my_turtle.fd(20)
my_turtle.left(135)
my_turtle.fd(20)
my_turtle.right(135)
my_turtle.fd(20)
my_turtle.left(135)
my_turtle.fd(20)
my_turtle.right(135)
my_turtle.fd(20)
my_turtle.left(135)
my_turtle.fd(20)
my_turtle.right(135)
my_turtle.fd(20)
my_turtle.left(135)
my_turtle.fd(20)
my_turtle.right(135)
my_turtle.fd(20)

# Exercise f
my_turtle.left(72)
my_turtle.fd(100)
my_turtle.right(144)
my_turtle.fd(100)
my_turtle.left(72)
my_turtle.fd(100)
my_turtle.right(144)
my_turtle.fd(100)
my_turtle.left(72)
my_turtle.fd(100)
my_turtle.right(144)
my_turtle.fd(100)
my_turtle.left(72)
my_turtle.fd(100)
my_turtle.right(144)
my_turtle.fd(100)
my_turtle.left(72)
my_turtle.fd(100)
my_turtle.right(144)
my_turtle.fd(100)

turtle.done()