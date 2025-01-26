# Lesson 7: Functions

## Learning Objectives
- Understand the parts of a function and its syntax
- Create Turtle drawings from functions
- Learn about making more modular code (good coding practice!)

## Introduction to Functions in Turtle
Functions in Python are blocks of reusable code that perform a specific task. They help in organizing code, making it more readable, and allowing for code reuse. The same applies within Turtle Graphics. You can use functions to contain blocks of code that draw out specific things.  

## Defining and Calling Functions
- **Defining a Function:** Functions are defined using the `def` keyword, followed by the function name and parentheses `()`. The code block within every function is indented.
- **Calling a Function:** This is when you ask Python to run the code inside the function. You do this by using the function name followed by parentheses.  

Try running the following code:
```python
def greet():
    print("Hello, world!")

# Calling the function
greet() # prints "Hello, world!"
```

Functions can also take parameters, which are values you can pass into the function. These values are used as variables within the function.  

Try running the following code:
```python
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with a parameter
greet("Alice") # prints "Hello, Alice!"
```

## Additional Explanation: Baking Analogy
If you found the previous explanations confusing, this section uses a baking analogy to explain the concepts.  

Think about defining functions like creating recipes for baking: you haven't baked a cake yet, but you do have the recipe for it.  

Calling a function is like baking (executing) one cake from the recipe (function) that you have.  

Passing in parameters is like adding ingredients to your cake to get the final output. You want the cake that you're making right now to have flour, butter, and chocolate. Other times you might want to change the ingredients in your cake to have flour, butter, and blueberries instead.  

For both cakes, you follow a general recipe with the same set of steps (your initial function and the code block indented under it), and all you change are your ingredients (the parameters you pass into the function).

## Functions and Turtle Graphics
As mentioned, functions can be used to create more complex drawings with the Turtle Graphics library. For example, you can define a function to draw a square and then call it multiple times to draw multiple squares.

```python
import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Drawing two squares
draw_square(100) # draws the first square
turtle.penup()
turtle.forward(150)
turtle.pendown()
draw_square(100) # draws the second square

turtle.done()
```

## Review

### Question 1
What is the purpose of defining a function in Python?  
a. To create a new variable  
b. To execute a block of code  
c. To define a new data type  
d. To create a new loop

<details>
<summary>Answer</summary>
b
</details>

### Question 2
How do you call a function in Python?  
a. By using the `def` keyword  
b. By using the function name followed by parentheses  
c. By using the `call` keyword  
d. By using the `execute` keyword

<details>
<summary>Answer</summary>
b
</details>

### Question 3
What does the number in the parentheses of a `forward` or `backward` command represent in Turtle Graphics?  
a. How many degrees the turtle is supposed to turn  
b. How fast the turtle is supposed to move  
c. How far the turtle is supposed to move  
d. The color of the turtle

<details>
<summary>Answer</summary>
c
</details>

### Question 4
Which of the following is NOT a command you can give to the turtle?  
a. `turn`  
b. `color`  
c. `backward`  
d. `left`

<details>
<summary>Answer</summary>
a
</details>

### Question 5
Which of the following statements is true about indentation in Python?  
a. Indentation only matters in for loops. Then, everything must be indented one level.  
b. Indentation never matters in Python. You can align your code any way you like, but indentation makes your code easier to read.  
c. Indentation always matters in Python. Every statement must be aligned correctly.  
d. Indentation only matters in functions. Then, everything must be indented one level.

<details>
<summary>Answer</summary>
c
</details>

## Exercise

a. (Easy) Make 3 functions to draw a square, a circle, and a triangle. No parameters are required yet.

<details>
<summary>Hint</summary>
You can use any previous code you've written. Since there are no parameters that need to be passed in for now, you can leave the parentheses after the function name empty.
</details>

b. (Medium) Call the functions in the same sequence to create a drawing where the 3 shapes are spaced apart by 100 units.

<details>
<summary>Hint</summary>
Add lines of code between calling the functions to space apart the shapes (like in the example above).
</details>

c. (Hard) Create a function that draws a hexagon. 3 parameters should be passed in: the side length of the hexagon, the x coordinate of the hexagon, and the y coordinate of the hexagon. Call it.

<details>
<summary>Hint</summary>
Since you need to pass in parameters now, the parentheses after the function name should now contain these 3 variables.
</details>