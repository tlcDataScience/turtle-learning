import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

for i in range(3):
    my_turtle.fd(100)
    my_turtle.left(120)

turtle.done()