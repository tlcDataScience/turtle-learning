# Lesson 12: Project - Pong Game

## Learning Objectives
- Learn how to use Visual Studio Code to run programs
- Fill in lines of code using the Turtle concepts learned in this course
- Be exposed to the basics of game development

Up to this point, you've mostly used trinket.io to run code, but there are times online compilers do not contain the full set of capabilities required to run a program. As a result, it's also important to know how to run code on a code editor installed on your laptop. You will be using Visual Studio Code (also known as VS Code) to run this project.

## Project Brief
In this project, you will be creating a two-player Pong Game using Turtle Graphics.
- **Description:** In the game, the players move paddles up and down to keep a ball within the playing area.
- **Scoring:** A player gains a point when the opponent misses the ball.
- **Objective:** The goal is to defeat your opponent by getting the highest score.
- You can try the game here: https://www.ponggame.org/
    - Left paddle controls: Press the "s" key to move the paddle upwards and the "x" key to move the paddle downwards.
    - Right paddle controls: Press the "up" arrow key to move the paddle upwards and the "down" arrow key to move the paddle downwards.
    - For the game that you create, you can change the keys that control the turtle's movement under the `Keyboard bindings` section.

Since this course focuses on introducing Turtle concepts and does not cover game planning and development, you will be downloading a file then filling in specific lines of code according to the given instructions.  

For example, given the block of code:

```python
# Left paddle
left_pad = turtle.Turtle() # Creates a turtle to serve as the left paddle
# TO DO: Change the pen speed to the fastest setting
# TO DO: Change the turtle shape to a square
```

You are expected to come up with the following:

```python
# Left paddle
left_pad = turtle.Turtle() # Creates a turtle to serve as the left paddle
# TO DO: Change the pen speed to the fastest setting
left_pad.speed(0)
# TO DO: Change the turtle shape to a square
left_pad.shape("square")
```

The `#` symbol indicates that the specific line of code is a comment. A comment is a line of code that does not get executed. It's good coding practice to use comments to label and organize your code.

> Check the comments for instructions on how to create each component in the game. You'll need to fill them in accordingly.

With that, let's get started!

## Steps

### Step 1
From the Lesson 12 folder (this folder), download the file called "PongGameStudent.py".

### Step 2
Open the file on Visual Studio Code.
> Refer to Lesson 0 for the setup instructions.

### Step 3
Write your lines of code under each of the instructions. Make sure not to delete any line from the original file to help with any debugging required later on.

### Step 4
Click `Ctrl + F` and search for `# TO DO:` to ensure you haven't missed out on anything.

### Debugging Tips
- While testing your game, there may be times you see an issue that you want to fix right away before your code is finished executing. You can press the "Stop" button (red square in the Visual Studio Code top menu) for this.
- Understand what may have gone wrong by reading the error message in the Terminal. It may give a clue to the line number/s that have issues.
- Check if all of your variable names are consistent. Variables names are case-sensitive, so errors here will cause issues in running the code.
- Check your code indentation levels (`Tab` to shift inwards, `Shift + Tab` to shift outwards). You may have accidentally moved something to the wrong place.
- As always, you may reference the Scripts (Answer Key) > Lesson 12 Scripts folder in this repository if all of the above are not working.

## Review

### Question 1
After creating each paddle (left and right), why must your turtle's pen be lifted up?

<details>
<summary>Answer</summary>
You wouldn't want your paddle to draw unnecessary lines while you're moving it during the game.
</details>

### Question 2
How are different objects created on the screen?

<details>
<summary>Answer</summary>
Different turtles are created for each of them.
</details>

### Question 3
You may have seen new commands you haven't learned before: `turtle.write()` and `screen.listen()`. What do you think these do?
<details>
<summary>Answer</summary>
<code>turtle.write()</code>: Used to write text at the current turtle position  
<code>screen.listen()</code>: Used to focus on the TurtleScreen in order to collect key-events (receives information on which key was pressed to correctly control the turtle/paddles)
</details>

## Demo
Run your game and ensure that everything is working properly!

## Exploring More
Turtle Graphics is a powerful tool that can do much more than just draw shapes. You can create games, animations, and even interactive programs. As you learn more, you can explore the `turtledemo` package which includes a set of demo scripts that showcase different features of the Turtle module.

> Remember, the best way to learn is by doing. So, keep experimenting with different commands and see what you can create!

Congratulations! You have completed The Logic Coders - Introduction to Python Turtle!  
-- END --