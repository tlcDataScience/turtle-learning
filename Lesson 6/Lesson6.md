# Lesson 6: While Loops

## Learning Objectives
- Learn the concept of while loops
- Understand how to use while loops to repeat Turtle movements as learned in Lessons 1 & 2
- Combine knowledge of conditional statements (Lesson 4) and for loops (Lesson 5) to customize drawings of regular polygons

### While Loops

In this lesson, you will cover the basics of using `while` loops, a control structure that allows for indefinite iteration. This means the loop will continue to execute as long as the condition specified remains true.

### Basic Structure of a While Loop
A `while` loop starts with the keyword `while`, followed by a condition that must evaluate to `True` for the loop to execute. The code block to be executed is indented under the `while` statement. Here's a simple example:

```python
n = 5 # declares 5 as the initial value of n
while n > 0: # checks whether the value of n is greater than 0
    n = n - 1 # subtracts 1 from the current value of n
    print(n)
```

In this example, the loop will continue to execute as long as `n` is greater than 0. Each iteration decrements (decreases) `n` by 1 and prints its value.

Important things to note:
- Condition: The condition must be placed right after the `while` keyword and before the colon (`:`). It's crucial for the loop to know when to stop executing.
- Indentation: The code block under the `while` loop must be indented. Python uses indentation to define blocks of code.
- Colon (`:`): Don't forget the colon after the condition. It's part of Python's syntax for defining blocks of code.

### Interrupting Loop Execution

You can control the flow of a `while` loop using `break` and `continue` statements:

- `break`: Exits the loop prematurely.
- `continue`: Skips the rest of the current iteration and moves on to the next iteration.

These functions are for your information (FYI) only. They jump into the code and break the loop logic, so they're not usually recommended for use unless absoluely required. Just know that there are other ways of going about writing these.

### Dealing with Infinite Loops

Be cautious with `while` loops, as they can create infinite loops if the condition never becomes false. Always ensure there's a way for the loop to terminate.

### For Loops vs While Loops

You have learned two types of loops so far, so what are their differences, and how do you know which one to use?

![For-vs-While-Loop](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/a7c62181-3dc3-4c3d-80d4-f6b3f84e11f7)
<img src="https://github.com/The-Logic-Coders/turtle-program/assets/97239180/99952eb9-05b8-4a74-9d6f-3c6f584c9e10" width="550">

## Review

### Question 1
What is the purpose of a `while` loop in Python?  
a. To execute a block of code a specific number of times.  
b. To execute a block of code as long as a condition is true.  
c. To execute a block of code once.  
d. To execute a block of code in reverse order.

<details>
<summary>Answer</summary>
b
</details>

### Question 2
What is the correct syntax for a `while` loop in Python?  
a. `while (condition):`  
b. `while condition:`  
c. `while {condition}`  
d. `while condition {}`

<details>
<summary>Answer</summary>
b
</details>

### Question 3
What happens if the condition in a `while` loop is never met?  
a. The loop will execute indefinitely.  
b. The loop will execute once.  
c. The loop will not execute at all.  
d. The loop will execute twice.

<details>
<summary>Answer</summary>
c
</details>

### Question 4
What is the output of the following Python code?

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

a. 0 1 2 3 4  
b. 0 1 2 3 4 5  
c. 0 1 2 3 4 5 6  
d. 1 2 3 4

<details>
<summary>Answer</summary>
a
</details>

### Question 5
What is the output of the following Python code?

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        count = 6
    print(count)
```

a. 1 2 3 4 5  
b. 1 2 3 4 5 6  
c. 1 2 6  
d. 1 2 3

<details>
<summary>Answer</summary>
c
</details>

## Exercise

The same, but different.  

### Part 1
Complete Challenges 10-14 from Lesson 3. This time, use `while` loops and the commands you've learnt so far. Look at that Lesson page (Lesson 3) to understand how the shapes are constructed (click the dropdown arrows to see the GIFs).

### Part 2
Create a program that draws regular polygons with user-defined number of sides. For example, if a user inputs 3, then a triangle should be drawn since it has 3 sides. This exercise aims to test your ability to perform data validation using conditional statements that we learned in Lesson 4 and combine that with your new knowledge of loops. Here are a few points to keep in mind:
1. The user must input a number of sides (integer) greater than 2 to generate a polygon.
2. Each time a valid input is given, the screen must reset to draw the new shape.
3. If the number of sides is odd, draw the polygon in blue. If the number of sides is even, draw the polygon in red.
4. A negative input can be received, but a message should appear to direct the user to the accepted range of inputs.
5. Polygons with 0, 1, or 2 sides do not exist.
6. Make the user re-input a number if the current input is invalid or not equal to -1.
7. When the user inputs -1, the program should terminate.
8. Assume the user will always input an integer.

<details>
<summary>Hint</summary>
Attempt each challenge first. If you are stuck, you can refer to the Scripts (Answer Key) > Lesson 3 Scripts folder, where there will be a sample solution for each of the challenges (only one of the many ways that you can create each image!). This exercise is meant to boost your creativity and learn programming concepts using Turtle along the way!
</details>