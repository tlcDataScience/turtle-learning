import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

turtle_colors = ["red", "yellow", "blue", "green", "light blue", "pink"]

i = 0

while i < 12:
    my_turtle.color(turtle_colors[i % 6])
    my_turtle.circle(50)
    my_turtle.penup()
    my_turtle.fd(20)
    my_turtle.pendown()
    i += 1

turtle.done()