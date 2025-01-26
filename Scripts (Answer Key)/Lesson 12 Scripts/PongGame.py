# Import required library/module
import turtle


# Create a screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("white")
screen.setup(1000, 600)


# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Circular ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5


# Initialize the score
left_player = 0
right_player = 0


# Display the score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("blue")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Left_player: 0 | Right_player: 0",
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
screen.listen()
screen.onkeypress(paddleaup, "s")
screen.onkeypress(paddleadown, "x")
screen.onkeypress(paddlebup, "Up")
screen.onkeypress(paddlebdown, "Down")


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
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		left_player += 1
		scoreboard.clear()
		scoreboard.write("Left_player: {} | Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

	if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
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