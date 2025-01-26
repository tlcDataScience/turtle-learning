import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

turtle_colors = ["red", "yellow", "blue", "green", "light blue", "pink"]

i = 0

while i < 6:
    j = 0
    my_turtle.color(turtle_colors[i])
    while j < 6:
        my_turtle.left(60)
        my_turtle.fd(120 - 20 * i)
        my_turtle.left(120)
        my_turtle.fd(120 - 20 * i)
        my_turtle.left(120)
        my_turtle.fd(120 - 20 * i)
        j += 1
    i += 1

turtle.done()