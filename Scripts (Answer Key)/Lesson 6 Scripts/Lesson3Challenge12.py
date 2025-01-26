import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

i = 10 # Start distance value

while i < 350:
    my_turtle.fd(i)
    i += 10
    my_turtle.right(90)

turtle.done()