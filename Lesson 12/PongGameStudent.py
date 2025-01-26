# Import required library/module
# TO DO: Import the Turtle module


# Create a screen
screen = turtle.Screen() # Creates a screen
# TO DO: Change the screen title to "Pong Game"
# TO DO: Change the background color to white
screen.setup(1000, 600) # Sets the dimensions of the screen


# Left paddle
left_pad = turtle.Turtle() # Creates a turtle to serve as the left paddle
# TO DO: Change the pen speed to the fastest setting
# TO DO: Change the turtle shape to a square
# TO DO: Set the pen color to black
# TO DO: Change the turtle size to have a stretch width of 6 and a stretch length of 2
# TO DO: Lift your turtle's pen up
# TO DO: Move the turtle to the (-400, 0) location on the screen


# Right paddle
right_pad = turtle.Turtle() # Creates a turtle to serve as the right paddle
# TO DO: Change the pen speed to the fastest setting
# TO DO: Change the turtle shape to a square
# TO DO: Set the pen color to black
# TO DO: Change the turtle size to have a stretch width of 6 and a stretch length of 2
# TO DO: Lift your turtle's pen up
# TO DO: Move the turtle to the (400, 0) location on the screen


# Circular ball
hit_ball = turtle.Turtle() # Creates a turtle to serve as the ball
# TO DO: Change the pen speed to 40
# TO DO: Change the turtle shape to a circle
# TO DO: Set the pen color to blue
# TO DO: Lift your turtle's pen up
# TO DO: Move the turtle to the (0, 0) location on the screen
hit_ball.dx = 5 # Defines how the ball moves in the x direction
hit_ball.dy = -5 # Defines how the ball moves in the y direction


# Initialize the score
# TO DO: Initialize a variable called left_player with a value of 0
# TO DO: Initialize a variable called right_player with a value of 0


# Display the score
scoreboard = turtle.Turtle() # Creates a turtle to serve as the scoreboard
# TO DO: Change the pen speed to the fastest setting
# TO DO: Set the pen color to blue
# TO DO: Lift your turtle's pen up
scoreboard.hideturtle() # Hides the turtle to display the text only
# TO DO: Move the turtle to the (0, 260) location on the screen
scoreboard.write("Left_player: 0 | Right_player: 0", # Formats the scoreboard
	align="center", font=("Courier", 24, "normal"))


# Functions to move paddles vertically
def paddleaup():
	y = left_pad.ycor()
	y += 20
	left_pad.sety(y)


def paddleadown():
	y = left_pad.ycor()
	y -= 20
	left_pad.sety(y)


def paddlebup():
	y = right_pad.ycor()
	y += 20
	right_pad.sety(y)


def paddlebdown():
	y = right_pad.ycor()
	y -= 20
	right_pad.sety(y)


# Keyboard bindings
screen.listen() # Collects key-events
screen.onkeypress(paddleaup, "s") # "s" key moves left_pad upwards
screen.onkeypress(paddleadown, "x") # "x" key moves left_pad downwards
screen.onkeypress(paddlebup, "Up") # "up" arrow key moves right_pad upwards
screen.onkeypress(paddlebdown, "Down") # "down" arrow key moves right_pad downwards


# Main gameplay
while True:
	screen.update()

	hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
	hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

	# Check borders
	if hit_ball.ycor() > 280:
		hit_ball.sety(280)
		hit_ball.dy *= -1

	if hit_ball.ycor() < -280:
		hit_ball.sety(-280)
		hit_ball.dy *= -1

	if hit_ball.xcor() > 500:
		# TO DO: Move the hit_ball turtle to the (0, 0) location on the screen
		hit_ball.dy *= -1
		left_player += 1
		scoreboard.clear()
		scoreboard.write("Left_player: {} | Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

	if hit_ball.xcor() < -500:
		# TO DO: Move the hit_ball turtle to the (0, 0) location on the screen
		hit_ball.dy *= -1
		right_player += 1
		scoreboard.clear()
		scoreboard.write("Left_player: {} | Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

	# Paddle ball collision
	if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 90 and hit_ball.ycor() > right_pad.ycor() - 90):
		hit_ball.setx(360)
		hit_ball.dx *= -1
		
	if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 90 and hit_ball.ycor() > left_pad.ycor() - 90):
		hit_ball.setx(-360)
		hit_ball.dx *= -1

turtle.done()