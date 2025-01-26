# Import required libraries/modules
import turtle
import random

# Create a screen
screen = turtle.Screen()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800) # do not include if using trinket.io

# Player 1 turtle
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

# Player 2 turtle
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# Player 1 home base
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

# Player 2 home base
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# On-screen winner message
winner = turtle.Turtle()
winner.hideturtle()
winner.penup()
winner.goto(75, 200)

# Start drawing
player_one.pendown()
player_two.pendown()

# Create a die
die = [1, 2, 3, 4, 5, 6]

# Main gameplay
for i in range(20):
    # Check if Player 1 has won
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        winner.write("Player One Wins!", align="center", font=("Candara", 24, "bold"))
        break
    # Check if Player 2 has won
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        winner.write("Player Two Wins!", align="center", font=("Candara", 24, "bold"))
        break
    # Die roll and turtle movement
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player_one.fd(20 * die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player_two.fd(20 * die_outcome)

turtle.done()