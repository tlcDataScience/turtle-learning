# Import required libraries/modules
# TO DO: Import the Turtle module
import time
import random


# TO DO: Initialize a variable called delay with a value of 0.1
# TO DO: Initialize a variable called score with a value of 0
# TO DO: Initialize a variable called high_score with a value of 0


# Create a screen
screen = turtle.Screen() # Creates a screen
# TO DO: Change the screen title to "Snake Game"
# TO DO: Change the background color to blue
screen.setup(600, 600) # Sets the dimensions of the screen
screen.tracer(0) # Turns automatic screen updates off (0)


# Head of the snake
head = turtle.Turtle() # Creates a turtle to serve as the head of the snake
# TO DO: Change the turtle shape to a square
# TO DO: Set the pen color to white
# TO DO: Lift your turtle's pen up
# TO DO: Move the turtle to the (0, 0) location on the screen
head.direction = "Stop"


# Food of the snake
food = turtle.Turtle() # Creates a turtle to serve as the food of the snake
colors = random.choice(['red', 'green', 'black']) # Possible colors of the turtle
shapes = random.choice(['square', 'triangle', 'circle']) # Possible shapes of the turtle
# TO DO: Change the pen speed to the fastest setting
# TO DO: Change the turtle shape to a randomized shape (check the variable above)
# TO DO: Set the pen color to a randomized color (check the variable above)
# TO DO: Lift your turtle's pen up
# TO DO: Move the turtle to the (0, 100) location on the screen


# Display the score
scoreboard = turtle.Turtle() # Creates a turtle to serve as the scoreboard
# TO DO: Change the pen speed to the fastest setting
# TO DO: Change the turtle shape to a square
# TO DO: Set the pen color to white
# TO DO: Lift your turtle's pen up
scoreboard.hideturtle() # Hides the turtle to display the text only
# TO DO: Move the turtle to the (0, 250) location on the screen
scoreboard.write("Score: 0 | High Score: 0", # Formats the scoreboard
    align="center", font=("Candara", 24, "bold"))


# Assign key directions
def go_up():
	if head.direction != "down":
		head.direction = "up"


def go_down():
	if head.direction != "up":
		head.direction = "down"


def go_left():
	if head.direction != "right":
		head.direction = "left"


def go_right():
	if head.direction != "left":
		head.direction = "right"


def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)


# Keyboard bindings
screen.listen() # Collects key-events
screen.onkeypress(go_up, "w") # "w" key moves snake upwards
screen.onkeypress(go_down, "s") # "s" key moves snake downwards
screen.onkeypress(go_left, "a") # "a" key moves snake leftwards
screen.onkeypress(go_right, "d") # "d" key moves snake rightwards

segments = []


# Main gameplay
while True:
	screen.update()

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		# TO DO: Move the head turtle to the (0, 0) location on the screen
		head.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
		for segment in segments:
			segment.goto(1000, 1000)
		segments.clear()
		score = 0
		delay = 0.1
		scoreboard.clear()
		scoreboard.write("Score: {} | High Score: {} ".format(
			score, high_score), align="center", 
            font=("Candara", 24, "bold"))
		
	if head.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		# TO DO: Move the food turtle to the (x, y) location on the screen

		# Add new snake segment
		new_segment = turtle.Turtle() # Creates a turtle to serve as the new body segment
		# TO DO: Change the pen speed to the fastest setting
        # TO DO: Change the turtle shape to a square
        # TO DO: Set the pen color to orange
        # TO DO: Lift your turtle's pen up
		segments.append(new_segment)
		delay -= 0.001
		score += 10

		if score > high_score:
			# TO DO: Assign the current score as the new high_score
		scoreboard.clear()
		scoreboard.write("Score: {} | High Score: {} ".format(
			score, high_score), align="center", 
            font=("Candara", 24, "bold"))
		
	# Check for head collisions with body segments
	for index in range(len(segments) - 1, 0, -1):
		x = segments[index - 1].xcor()
		y = segments[index - 1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			# TO DO: Move the head turtle to the (0, 0) location on the screen
			head.direction = "Stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
			for segment in segments:
				segment.goto(1000, 1000)
			segments.clear()

			score = 0
			delay = 0.1
			scoreboard.clear()
			scoreboard.write("Score: {} | High Score: {} ".format(
				score, high_score), align="center", 
                font=("Candara", 24, "bold"))
	time.sleep(delay)

screen.mainloop()