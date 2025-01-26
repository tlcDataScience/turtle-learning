# Lesson 0: Introduction to Turtle Graphics

## Learning Objectives
- Understand what Turtle is and why it's used in programming
- Know how to use the trinket.io online compiler for Turtle (main coding platform)
- Know how to set up a basic Turtle Graphics window on Visual Studio Code (in case trinket.io does not work)

> Note: For this module, you can use trinket.io and/or Visual Studio Code to compile and display your code. Refer to this lesson for setup instructions for subsequent lessons. Google Colab is not recommended as additional steps will be required to compile Turtle code.

> All review questions have answers which can be accessed by clicking on the toggle button below each question.

> All exercises and projects have full scripts which can be accessed by clicking on the Scripts (Answer Key) folder in this GitHub repository, then selecting the correct lesson. These are for reference and should only be used when you're really stuck! Always try to attempt the question first.

## What is Turtle Graphics?
The Turtle Graphics library in Python allows for the creation of simple graphics and drawings. You control a cursor, called a "turtle", which moves around the screen. As the turtle moves, it can draw lines and shapes, allowing you to create pictures and patterns. It's a fun and interactive way to learn programming concepts through drawing and animation.

## How to set up Turtle Graphics on trinket.io

### Step 1
Click on the following link to the trinket.io online compiler for Turtle: https://trinket.io/turtle

### Step 2
Remove any code that is currently on the screen.

### Step 3
Paste in the following template code, which is also available to view under the Scripts (Answer Key) > Lesson 0 Scripts folder in this repository.

```python
import turtle # imports the Turtle module
screen = turtle.Screen()
my_turtle = turtle.Turtle() # creates a turtle

# Set up the window
screen.setup(800, 600)

# INSERT CODE HERE

turtle.done()
```

### Step 4
Fill in your code under the line `# INSERT CODE HERE`.

### Step 5
Click the "Run" button, which is the triangle located on the left side of the menu.

### Optional
Click on the "Expand" button to increase the size of your Turtle Graphics screen if needed, which is located below the code and window sections. You're now ready to start coding with Turtle!

## How to set up Turtle Graphics on Visual Studio Code
To start using Turtle Graphics, you need to have Python and Visual Studio Code installed on your computer.
- Check if you have Python by opening the Windows Terminal and typing `python` in the command line. A version number `Python 3.x.x` should show up.
- Check if you have Visual Studio Code by searching for the application in the Windows menu bar.
- Follow this video for complete setup (if needed): https://youtu.be/Q8q8C236ieQ (disregard the next two bullet points if all works well)
- If you don't have Python, you can download it from the official website (https://www.python.org/downloads/).
- If you don't have Visual Studio Code, you can download it from the official website (https://code.visualstudio.com/download).

Once you have Python and Visual Studio Code, you can start using Turtle Graphics by following these steps:

### Step 1
Open Visual Studio Code and click on "New File..." then click "Python File" (adds the .py extension to your filename)

### Step 2
Paste in the following template code, which is also available to view under the Scripts (Answer Key) > Lesson 0 Scripts folder in this repository.

```python
import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Set up the window
screen.setup(800, 600)

# Set the canvas size
screen.screensize(1000, 800)

# INSERT CODE HERE

turtle.done()
```

### Step 3
Fill in your code under the line `# INSERT CODE HERE`.

### Step 4
Click the "Run" button and then select "Run Without Debugging" from the dropdown.

## Explanation of Template.py

### Step 1
**Import the Turtle Module**: At the beginning of your Python script, you need to import the Turtle module.

```python
import turtle
```

### Step 2
**Create a Screen**: Before you can draw with your turtle, you need to create a screen (also known as a window or canvas) for it to draw on.

```python
screen = turtle.Screen()
```

### Step 3
**Create a Turtle**: Now that you have a screen, you can create a turtle that will draw on it.

```python
my_turtle = turtle.Turtle()
```

### Step 4
**Set Window Size**: You can specify the width and height of the window, and optionally, the starting position of the window on the screen, using the function `screen.setup(width, height, startx, starty)`.

```python
# Set up the window
screen.setup(800, 600)
```

### Step 5 (only used to set up the drawing environment on Visual Studio Code, not on trinket.io)
**Set Canvas Size**: You can specify the width and height of the canvas using the function `screen.screensize(width, height)`. The width and height are specified in pixels. By default, the canvas size is 500x500 pixels.

```python
# Set the canvas size
screen.screensize(1000, 800)
```

> Note: All modules in this course will refer back to the initialization of `screen` and `my_turtle`, so don't get confused when a specific function or an answer starts with `my_turtle.` rather than only `turtle.`! Go to the Scripts (Answer Key) > Lesson 0 Scripts folder in this repository and copy the code from `Template.py` before starting any exercise in this course.

With these steps, you're all set up to start drawing with your turtle!

> Reference: Always refer to Turtle documentation (https://docs.python.org/3/library/turtle.html#turtle.screensize) to check whether a method is a Turtle method, a Screen method, etc.