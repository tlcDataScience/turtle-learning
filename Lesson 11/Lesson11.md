# Lesson 11: Project - Snake Game

## Learning Objectives
- Learn how to use Visual Studio Code to run programs
- Fill in lines of code using the Turtle concepts learned in this course
- Be exposed to the `time` and `random` modules, as well as the basics of game development

Up to this point, you've mostly used trinket.io to run code, but there are times online compilers do not contain the full set of capabilities required to run a program. As a result, it's also important to know how to run code on a code editor installed on your laptop. You will be using Visual Studio Code (also known as VS Code) to run this project.

## Project Brief
In this project, you will be creating a single-player Snake Game using Turtle Graphics.
- **Description:** In the game, the player moves a snake around the board.
- **Scoring:** As the snake finds food, it eats the food and grows larger, gaining points.
- **Objective:** The goal is to make the snake as large as possible before that happens.
- **Game End:** The game ends when the snake either moves off the screen or moves into itself.
- You can try the game here: https://playsnake.org/
    - Press the arrow keys to control the snake's movement.
    - For the game that you create, you can change the keys that control the turtle's movement under the `Keyboard bindings` section.

Since this course focuses on introducing Turtle concepts and does not cover game planning and development, you will be downloading a file then filling in specific lines of code according to the given instructions.  

For example, given the block of code:

```python
# Head of the snake
head = turtle.Turtle() # Creates a turtle to serve as the head of the snake
# TO DO: Change the turtle shape to a square
# TO DO: Set the pen color to white
```

You are expected to come up with the following:

```python
# Head of the snake
head = turtle.Turtle() # Creates a turtle to serve as the head of the snake
# TO DO: Change the turtle shape to a square
head.shape("square")
# TO DO: Set the pen color to white
head.color("white")
```

The `#` symbol indicates that the specific line of code is a comment. A comment is a line of code that does not get executed. It's good coding practice to use comments to label and organize your code.

> Check the comments for instructions on how to create each component in the game. You'll need to fill them in accordingly.

With that, let's get started!

## Steps

### Step 1
From the Lesson 11 folder (this folder), download the file called "SnakeGameStudent.py".

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
- As always, you may reference the Scripts (Answer Key) > Lesson 11 Scripts folder in this repository if all of the above are not working.

## About Modules/Libraries
For this project, you'll be using additional modules/libraries that add to the gameplay and overall game experience. Learn more about them below!

(Reference) When you go on to do more advanced programs after finishing this curriculum, you'll sometimes need functions beyond what is available in your lesson notes. If you're using Python, a good detailed resource to see all the functions you can use and how they work is Python Docs. Some links are provided for the ones used in this curriculum.
- Turtle documentation: https://docs.python.org/3/library/turtle.html
- Time documentation: https://docs.python.org/3/library/time.html
- Random documentation: https://docs.python.org/3/library/random.html

### Time Module
As the name suggests, the `time` module is a standard Python module that offers functions for accessing and converting time (working with time in general). It allows functionality like getting the current time, pausing the program from executing, etc. To use the module's functionalities, you need to import the Python `time` module. For this lesson, the following function will be used:

```python
import time
time.sleep(10) # Halt the execution of the program for 10 seconds
```

This function is used to add delay in the execution of a program. We can use it to halt the execution of the program for a given time in seconds, somewhat like "pausing" the program. Note that the function stops the execution of the current thread (block of code) only, not the whole program.

### Random Module
The `random` module can be used to perform random actions in Python such as generating random numbers, printing a random value from a list or string, etc. These are pseudo-random outputs, so that means they are not truly random (you don't need to go into this in depth, but just know that there's an algorithm that's used to generate the "randomness"). For this lesson, the following functions will be used:

```python
import random
colors = random.choice(['red', 'green', 'black']) # Randomly generate a color for the food of the snake within the specified list
shapes = random.choice(['square', 'triangle', 'circle']) # Randomly generate a shape for the food of the snake within the specified list
```

This function returns a random item from a list, tuple, or string.

```python
import random
x = random.randint(-270, 270) # Randomly generate an x coordinate for the food of the snake within the specified range (-270 and 270 are included)
y = random.randint(-270, 270) # Randomly generate a y coordinate for the food of the snake within the specified range (-270 and 270 are included)
```

This function returns an integer within the specified range, inclusive of the start and stop values. Note this slight difference from Python's built-in function `range()` where the stop value is excluded.

## Review

### Question 1
In line 16 of the Snake Game, if `screen.tracer(0)` turns automatic screen updates off, can you guess how you might replace the line of code if you wanted to turn automatic screen updates on instead? *(Hint: Think binary!)*

<details>
<summary>Answer</summary>
<code>screen.tracer(1)</code>
</details>

### Question 2
What does `time.sleep(delay)` do in this program, and how does it affect what the user sees on the screen?

<details>
<summary>Answer</summary>
<code>time.sleep(delay)</code> halts the execution of the program for <code>delay</code> seconds. It allows time for one frame of animation before starting over again with another round of gameplay. This is important because it ensures that everything looks smooth even when there are lots of objects moving around on-screen at once!
</details>

### Question 3
You've seen two different functions from the `random` module. For generating an x and y coordinate for the food of the snake, why would you use `randint()` over `choice()`?

<details>
<summary>Answer</summary>
It would be too time-consuming to list out all the integers from -270 to 270, so a range helps speed up that process (specifically for numbers).
</details>

## Demo
Run your game and ensure that everything is working properly!