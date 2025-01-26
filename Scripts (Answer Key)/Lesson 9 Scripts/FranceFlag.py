import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Start position
my_turtle.penup()
my_turtle.goto(-400, -240)
my_turtle.pendown()

# Blue, white, red rectangles
colors = ["blue", "white", "red"]
for i in range(len(colors)):
    my_turtle.color(colors[i])
    my_turtle.begin_fill()
    my_turtle.lt(90)
    my_turtle.fd(480)
    my_turtle.rt(90)
    my_turtle.fd(800 / 3)
    my_turtle.rt(90)
    my_turtle.fd(480)
    my_turtle.rt(90)
    my_turtle.fd(800 / 3)
    my_turtle.end_fill()
    my_turtle.penup()
    my_turtle.setheading(0)
    my_turtle.fd(800 / 3)
    my_turtle.pendown()

turtle.done()