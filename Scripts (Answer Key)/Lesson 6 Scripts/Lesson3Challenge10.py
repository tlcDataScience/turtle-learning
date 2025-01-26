import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

i = 0

while i < 6:
    my_turtle.left(60)
    my_turtle.fd(100)
    my_turtle.left(120)
    my_turtle.fd(100)
    my_turtle.left(120)
    my_turtle.fd(100)
    i += 1

turtle.done()