# Lesson 5: For Loops

## Learning Objectives
- Learn the concept of for loops
- Understand how to use for loops to repeat Turtle movements as learned in Lessons 1 & 2
- Be exposed to the more advanced concept of nested for loops

### For Loops

The lines of code in your files are generally executed from top to bottom, in the order that they appear. Control flow statements, however, break up the flow of execution by having decision making and looping, enabling your program to conditionally execute particular blocks of code.

In Python, a `for` loop is an example of a control flow statement that allows you to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence. This is a fundamental concept in Python programming, enabling you to perform repetitive tasks more efficiently.

> A `for` loop can help shorten your code whenever you notice that you have repetitive code blocks.

### Basic Syntax of a For Loop

The basic syntax of a `for` loop in Python is as follows:

```python
for variable in sequence:
    # YOUR CODE HERE - code block to execute for each item in the sequence
```

Here, `variable` is the variable that takes the value of the item inside the sequence on each iteration. The `sequence` is the iterable object you want to loop through, such as a list, tuple, or string.

### Example: Iterating Over a List

Let's consider a simple example where we have a list of programming languages and we want to print each language:

```python
languages = ['C+', 'Python', 'Java']

for language in languages:
    print(language)
```

In this example, `language` is the variable that takes the value of each item in the `languages` list on each iteration. The loop will print each language in the list.

Output:
```python
C+
Python
Java
```

### Example: Iterating Over a String

You can also use a `for` loop to iterate over a string, where each iteration will give you a single character. This loop will print each character in the `greeting` string on a new line.

```python
greeting = "Hello, World!"

for char in greeting:
    print(char)
```

Output:
```python
H
e
l
l
o
,

W
o
r
l
d
!
```

### Using the `range()` Function

Now that you understand a little bit more about how `for` loops work, you will learn how to apply them in your Turtle code.

Python also provides a built-in function called `range()` that generates a sequence of numbers, which can be used with a `for` loop to perform an action a specific number of times. The `range()` function can take one, two, or three arguments:

- `range(stop)`: Generates a sequence of numbers from 0 to `stop - 1`.
- `range(start, stop)`: Generates a sequence of numbers from `start` to `stop - 1`.
- `range(start, stop, step)`: Generates a sequence of numbers from `start` to `stop - 1`, incrementing (increasing) by `step`.

Here's an example using `range()`. This loop will print the numbers 0 through 4.

```python
for i in range(5):
    print(i)
```

Important things to note:
- The variable `i` will start from 0 by default if there is no `start` value defined. Other than the conventional `i`, you may use other variable names as shown above. This specific variable can also be referred to as a counter variable.
- The `stop` value itself is not included in the output. That is why when you write `range(5)`, the output shown is only until 4.
- The `step` value is `1` by default if it is not defined (i.e. counting 0, 1, 2, 3, and so on).
- If there is only one argument in the function, take it as the `stop` value (e.g. `range(3)` - includes 0, 1, 2).
- If there are two arguments in the function, take them as the `start` and `stop` values, respectively (e.g. `range(1, 3)` - includes 1, 2).
- If there are three arguments in the function, take the last value as the `step` value (e.g. `range(2, 10, 3)` - includes 2, 5, 8; `range(2, 10, 2)` - includes 2, 4, 6, 8).

### Application of For Loops in Turtle

Here's how you can draw a square:

```python
import turtle

# Create a screen and a turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Keep the window open
turtle.done()
```

### Nested For Loops
At times, you will need a more complex code to achieve your desired pattern. Nested loops in Python are loops that are placed inside another loop. In the context of Turtle Graphics, they are used to repeat a certain operation multiple times within another operation.

### Structure of Nested For Loops
The structure of a nested `for` loop involves an outer loop and one or more inner loops. The outer loop iterates over a sequence, and for each iteration of the outer loop, the inner loop(s) execute their iterations. Here's a basic structure:

```python
# outer loop
for outer_element in outer_sequence:
    # inner loop
    for inner_element in inner_sequence:
        # body of inner loop
    # body of outer loop
```

For example, say you would like to draw 5 squares of varying side length but all with the same starting point. A square has 4 sides, so this whole shape will require 1 outer loop and 1 inner loop.

```python
n = 10 # initial side length n

for i in range(5): # draw 5 squares with the same starting point but different length n
    for j in range(4): # draw 4 sides of a square
        my_turtle.fd(n)
        my_turtle.left(90)
    n += 10 # increases side length by 10 after the inner loop is completed
```

Understand the execution sequence:

Steps 1-5
- The first outer loop is executed (`i = 0`).
- The first inner loop is executed (`j = 0`).
- The second inner loop is executed (`j = 1`).
- The third inner loop is executed (`j = 2`).
- The fourth and final inner loop is executed (`j = 3`).

Steps 6-10
- The second outer loop is executed (`i = 1`).
- The first inner loop is executed (`j = 0`).
- The second inner loop is executed (`j = 1`).
- The third inner loop is executed (`j = 2`).
- The fourth and final inner loop is executed (`j = 3`).

Steps 11-15
- The third outer loop is executed (`i = 2`).
- The first inner loop is executed (`j = 0`).
- The second inner loop is executed (`j = 1`).
- The third inner loop is executed (`j = 2`).
- The fourth and final inner loop is executed (`j = 3`).

Steps 16-20
- The fourth outer loop is executed (`i = 3`).
- The first inner loop is executed (`j = 0`).
- The second inner loop is executed (`j = 1`).
- The third inner loop is executed (`j = 2`).
- The fourth and final inner loop is executed (`j = 3`).

Steps 21-25
- The fifth and final outer loop is executed (`i = 4`).
- The first inner loop is executed (`j = 0`).
- The second inner loop is executed (`j = 1`).
- The third inner loop is executed (`j = 2`).
- The fourth and final inner loop is executed (`j = 3`).

For each set of 5 steps, a new square is added to the pattern with increasing side length (increased by 10 each time).

## Review

### Question 1
Which of the following is the correct syntax for a basic `for` loop in Python?  
a. `for i = 0 to 5:`  
b. `for i in range(5):`  
c. `for i from 0 to 5:`  
d. `for i in 0..5:`

<details>
<summary>Answer</summary>
b
</details>

### Question 2
Which numbers does the following loop print?  
```python
for i in range(1, 7, 3):
    print(i)
```
a. 1, 2, 3, 4, 5, 6  
b. 1, 4, 7  
c. 0, 3, 6  
d. 1, 4

<details>
<summary>Answer</summary>
d
</details>

### Question 3
Which numbers does the following loop print?  
```python
for i in range(2, 10):
    print(i)
```
a. 2, 3, 4, 5, 6, 7, 8, 9, 10  
b. 2, 3, 4, 5, 6, 7, 8, 9  
c. 2  
d. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

<details>
<summary>Answer</summary>
b
</details>

### Question 4
True or False: Should the lines under the for loop be indented?

<details>
<summary>Answer</summary>
True
</details>

### Question 5
A student writes the following code for a `for` loop that will output the numbers 1, 2, 3, 4, 5 (separated by a new line).  

```python
for i in range(1, 6):
print(i)
```

Will her code work? If not, explain why.

<details>
<summary>Answer</summary>
The code will not work because the <code>print</code> line is not indented. The <code>for</code> loop will not be able to iterate through the variable <code>i</code> to get the desired output.
</details>

## Exercise

Complete Challenges 1-7, 13-14 from Lesson 3. This time, use `for` loops and the commands you've learnt so far. Look at those Lesson pages (Lesson 1, Lesson 3) to understand how the shapes are constructed (click the dropdown arrows to see the GIFs).

<details>
<summary>Hint</summary>
Attempt each challenge first. If you are stuck, you can refer to the Scripts (Answer Key) > Lesson 1 Scripts & Lesson 3 Scripts folders, where there will be a sample solution for each of the challenges (only one of the many ways that you can create each image!). This exercise is meant to boost your creativity and learn programming concepts using Turtle along the way!
</details>