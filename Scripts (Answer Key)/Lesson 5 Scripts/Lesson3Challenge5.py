import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

for i in range(5):
    my_turtle.fd(100)
    my_turtle.right(144) # 360 degrees divided by 5 sides then multiplied by 2

turtle.done()