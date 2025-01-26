# Lesson 4: Conditional Statements

## Learning Objectives
- Learn the concept of conditional statements in Python
- Understand how conditional statements can be used to enhance Turtle Graphics
- Take in user input within programs

## Introduction to Conditional Statements

Conditional statements are a basic concept in programming that allow code to execute differently based on certain conditions. In Python, the most common conditional statements are `if`, `elif`, and `else`. These statements check a condition and execute a block of code if the condition is met (`True` if met, `False` if not met). The code below shows what this will generally look like:

```python
if condition:
    # body of if statement
elif condition:
    # body of elif statement
else:
    # body of else statement
```

Time to go through each one in more detail!  

### If statement

Suppose we need to assign different grades to students based on their scores.

1. If a student scores above **90**, assign grade **A**.  
2. If a student scores above **75**, assign grade **B**.  
3. If a student scores above **65**, assign grade **C**.

You can write these tasks into an `if`statement. Each statement takes in a boolean condition.

```python
grade = 80 # The given student's score is 80
if grade > 90: # Checks if the score is above 90
    print("A") # Assigns grade A if the condition is met
if grade > 75: # Checks if the score is above 75
    print("B") # Assigns grade B if the condition is met
if grade > 65: # Checks if the score is above 65
    print("C") # Assigns grade C if the condition is met
```

In this case, since the student's score is 80, the second (> 75) and third (> 65) `if` conditions are met (True), while the first condition is not (False). The code will output `B` and `C`.  

The student can only have 1 grade and cannot get both `B` and `C` grades, so how can we fix this?

> Note: Remember to indent the block of code under an `if` statement. This shows that the code is the body of the `if` statement. You can do this by pressing the "Tab" key or by pressing the space bar 4 times.

### Elif statement

When you have more than one condition to check, you can use an `elif` statement with your `if` statement. With an `elif` statement, the code can continuously run through your code to check which condition is met. If the first condition is not met, it will move on to the second condition. If the second condition is not met, it will move on to the third condition, and so on. Once one of these conditions is met, the rest of the code will be skipped.  

Using the same problem as above, the code can be rewritten:

```python
grade = 80 # The given student's score is 80
if grade > 90: # Checks if the score is above 90
    print("A") # Assigns grade A if the condition is met
elif grade > 75: # Checks if the score is above 75
    print("B") # Assigns grade B if the condition is met
elif grade > 65: # Checks if the score is above 65
    print("C") # Assigns grade C if the condition is met
```

The code above outputs the grade `B` only, which is correct. It now works for scores that are above 65. What happens when the score is 65 and below? Try to see what the code will output by changing the score in `grade = 80` to `grade = 65`.  

You should see that there is no output. This is because the score 65 does not meet any of the three conditions.

### Else statement

To fix the problem above, you can use an `else` statement to include all the other cases when all of your conditions are not met (False). "Else" can also be thought of as "otherwise." IF a condition is met, do code block 1. ELSE/OTHERWISE, do code block 2.  

Suppose a `C` is the minimum passing grade, and any score that is 65 and below is considered an `F`.

```python
grade = 80 # The given student's score is 80
if grade > 90: # Checks if the score is above 90
    print("A") # Assigns grade A if the condition is met
elif grade > 75: # Checks if the score is above 75
    print("B") # Assigns grade B if the condition is met
elif grade > 65: # Checks if the score is above 65
    print("C") # Assigns grade C if the condition is met
else:
    print("F") # Assigns grade F if none of the above conditions are met
```

Unlike the `if` and `elif` statements, the `else` statement does not need a condition to check. It will cover all other values.  

## Using Conditional Statements for Turtle

Combining conditional statements and Turtle Graphics help create a wide range of patterns and designs.  

You will cover loops in the following lessons, so for now, just know that loops help the pattern repeat to create your final drawing.  

If you have a pattern where every other statement alternates, you can use use the values of the step variable (i.e. `i` in a for loop) to determine if the value of the variable is odd or even.  

This code draws a zigzag line that moves forward by 25 units and turns right by 45 degrees for 10 iterations.

```python
import turtle
my_turtle = turtle.Turtle()

for i in range(10): # i takes on values from 0 to 9
    if i % 2 == 0: # Checks whether i is an even number
        my_turtle.fd(25)
        my_turtle.right(45)
    else: # Runs when i is not an even number (odd number)
        my_turtle.fd(25)
        my_turtle.left(45)
```

![Lesson 4 1 Zigzag](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/d18c6a62-be41-4a0f-964d-6c2486fd1e70)

Here's another example. This code draws a 9-point star.

```python
import turtle
my_turtle = turtle.Turtle()

for i in range(18): # i takes on values from 0 to 17
    my_turtle.fd(100)
    if i % 2 == 0:
        my_turtle.left(175)
    else:
        my_turtle.left(225)
```

![Lesson 4 2 9 Point Star](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/937396d5-9b0d-4c48-b842-800ca85fda64)

## Review

### Question 1
What happens if you do not indent a `print` statement under an `if` statement?  
a. The code will throw an error.  
b. The code will run if the condition is met.  
c. The code will run regardless of whether the condition is met.
d. The code will not output anything.

<details>
<summary>Answer</summary>
c
</details>

### Question 2
In a Turtle Graphics program, what does the `else` statement do if none of the `if` or `elif` conditions are met?  
a. It executes the code block immediately after the else statement.  
b. It executes the code block immediately before the else statement.  
c. It does nothing and skips the code block after it.  
d. It throws an error.

<details>
<summary>Answer</summary>
a
</details>

### Question 3
What is the purpose of the `elif` statement in the context of Turtle Graphics?  
a. To check if a condition is true, and if not, to check another condition.  
b. To check if a condition is false, and if not, to check another condition.  
c. To execute a block of code if the previous `if` condition was false.  
d. To execute a block of code if the previous `elif` condition was false.

<details>
<summary>Answer</summary>
a
</details>

### Question 4
What is the correct order of execution for the following `if`, `elif`, and `else` statements in a Turtle Graphics program?  
a. `condition1` -> `condition2` -> `else`  
b. `condition2` -> `condition1` -> `else`  
c. `condition1` -> `else` -> `condition2`  
d. `condition2` -> `else` -> `condition1`

<details>
<summary>Answer</summary>
a
</details>

### Question 5
True or False: An `elif` statement can be used without an `if` statement before it.

<details>
<summary>Answer</summary>
False
</details>

## Exercise

a. (Easy) Draw a simple zigzag pattern using a turtle. The turtle should move forward by 10 units and turn right by 90 degrees for 20 iterations.
<details>
<summary>Hint</summary>
Modify the previous code for the zigzag line.
</details>

b. (Easy) Create a colorful zigzag pattern. Use different colors for each iteration. Do not use a loop for this.
<details>
<summary>Hint</summary>
Copy and paste your block of code in between changing pen colors.
</details>

c. (Medium) Draw an 8-point star.
<details>
<summary>Hint</summary>
Modify the previous code for the 9-point star. Play with the angle values!
</details>

d. (Hard) Design an interactive pattern that changes based on user input. The user should be able to input the number of sides for a regular polygon (shape), and the turtle should draw that polygon. Use conditional statements to handle different numbers of sides. If the number of sides is odd, draw the polygon in blue. If the number of sides is even, draw the polygon in red.
<details>
<summary>Hint</summary>
Use the Python function <code>input()</code> to help with this. Each angle in a polygon with n sides is <code>((n - 2) * 180) / n</code>.
</details>