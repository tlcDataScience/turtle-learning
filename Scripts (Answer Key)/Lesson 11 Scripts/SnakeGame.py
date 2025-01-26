# Import required libraries/modules
import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0


# Create a screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("blue")
screen.setup(600, 600)
screen.tracer(0)


# Head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


# Food of the snake
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)


# Display the score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 250)
scoreboard.write("Score: 0 | High Score: 0",
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
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

segments = []


# Main gameplay
while True:
	screen.update()

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
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
		food.goto(x, y)

		# Add new snake segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("orange") # Tail color
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		score += 10

		if score > high_score:
			high_score = score
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
			head.goto(0, 0)
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