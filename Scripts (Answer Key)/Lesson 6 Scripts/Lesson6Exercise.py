import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Exercise
# Make sure all cases are accounted for (data validation)
# Users can enter -1 to terminate the program
n = -2
while n != -1:
    n = int(input("Please enter a number: "))
    if n == -1:
        print("The program will terminate now.")
    elif n == 0 or n == 1 or n == 2:
        print("No such polygon exists.")
    elif n > 0:
        my_turtle.reset()
        if n % 2 == 0:
            my_turtle.color("red")
        else:
            my_turtle.color("blue")
        for i in range(n):
            my_turtle.fd(50)
            my_turtle.left(180 - (((n - 2) * 180) / n))
    else:
        print("Please enter a positive integer greater than 2.")