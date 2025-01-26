import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

n = 10 # initial side length n

for i in range(5): # draw 5 squares with the same starting point but different length n
    for j in range(4): # draw 4 sides of a square
        my_turtle.fd(n)
        my_turtle.left(90)
    n += 10 # increases side length by 10 after the inner loop is completed

turtle.done()