import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Exercise a
for i in range(20): # i takes on values from 0 to 19
    if i % 2 == 0: # Checks whether i is an even number
        my_turtle.fd(10)
        my_turtle.right(90)
    else: # Runs when i is not an even number (odd number)
        my_turtle.fd(10)
        my_turtle.left(90)

# Exercise b
my_turtle.color("red")
my_turtle.fd(10)
my_turtle.right(90)
my_turtle.color("yellow")
my_turtle.fd(10)
my_turtle.left(90)
my_turtle.color("blue")
my_turtle.fd(10)
my_turtle.right(90)
my_turtle.color("green")
my_turtle.fd(10)
my_turtle.left(90)
my_turtle.color("light blue")
my_turtle.fd(10)
my_turtle.right(90)
my_turtle.color("pink")
my_turtle.fd(10)
my_turtle.left(90)
my_turtle.color("red")
my_turtle.fd(10)
my_turtle.right(90)
my_turtle.color("yellow")
my_turtle.fd(10)
my_turtle.left(90)
my_turtle.color("blue")
my_turtle.fd(10)
my_turtle.right(90)
my_turtle.color("green")
my_turtle.fd(10)
my_turtle.left(90)
my_turtle.color("light blue")
my_turtle.fd(10)
my_turtle.right(90)
my_turtle.color("pink")
my_turtle.fd(10)
my_turtle.left(90)

# Exercise c
for i in range(16): # i takes on values from 0 to 15
    my_turtle.fd(100)
    if i % 2 == 0:
        my_turtle.left(135)
    else:
        my_turtle.left(270)

# Exercise d
n = int(input("Please enter a number: "))
if n == 0:
    my_turtle.color("red")
    my_turtle.circle(50)
elif n % 2 == 0:
    my_turtle.color("red")
else:
    my_turtle.color("blue")
for i in range(n):
    my_turtle.fd(50)
    my_turtle.left(180 - (((n - 2) * 180) / n))

turtle.done()