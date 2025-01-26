# Lesson 3: Compilation of Lessons 1 & 2

## Learning Objectives
- Strengthen knowledge of constructing shapes from the commands taught in Lessons 1 & 2
- Complete drawing challenges with more complex shapes
- Establish good coding practices: Plan the drawing > Implement it in code form > Adjust where required

## Final Turtle Commands

**Undo Changes**: Undo the most recent action you did. If you want to undo your last five commands, then type `my_turtle.undo()` five times.

```python
my_turtle.forward(100)
my_turtle.undo()
```

**Clear Screen**: Clear your turtle to make room for more drawings. Your variables will not change, and the turtle will remain in the same position. If you have multiple turtles on the screen, then you need to call the specific turtle you want to clear.

```python
my_turtle.clear() # Clear my_turtle
```

**Reset Environment**: Remove all drawings from the screen to start from scratch. All parameters will be returned to their default values.

```python
my_turtle.reset()
```

**Leave a Stamp**: Leave a stamp of your turtle on the screen to trakc your actions.

```python
my_turtle.stamp()
my_turtle.fd(100)
my_turtle.stamp()
my_turtle.fd(100)
```

**Clear a Stamp**: Clear a particular stamp using its stamp ID.

```python
my_turtle.clearstamp(1) # Clear stamp with a stamp ID of 1
```

**Clone**: There are times when you need another turtle, and that is where this function comes in handy. The clone's parameters can be changed independent of the initial turtle.

```python
second_turtle = my_turtle.clone() # Clone my_turtle to make a second turtle called second_turtle
my_turtle.color("red")
second_turtle.color("blue")
my_turtle.circle(100)
second_turtle.circle(60)
```

![Lesson 3 1 Clone](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/e0efa7a5-f60f-426e-8a02-659250901ffa)

## Review

### Question 1
What does the `.undo()` function do in Turtle Graphics?  
a. It clears the screen.  
b. It undoes the last turtle movement.  
c. It resets the turtle to its original position.  
d. It clears all stamps.

<details>
<summary>Answer</summary>
b
</details>

### Question 2
What happens when you call `.undo()` after using `.stamp()`?  
a. The stamp is removed.  
b. The turtle's movement is undone.  
c. The turtle's position is reset.  
d. The screen is cleared.

<details>
<summary>Answer</summary>
a
</details>

### Question 3
What does the `.clear()` function do in Turtle Graphics?  
a. It clears the screen.  
b. It clears the last turtle movement.  
c. It resets the turtle to its original position.  
d. It clears all stamps.

<details>
<summary>Answer</summary>
a
</details>

### Question 4
What does the `.clone()` function do in Turtle Graphics?  
a. It creates a copy of the turtle at its current position.  
b. It clears the screen.  
c. It resets the turtle to its original position.  
d. It clears all stamps.

<details>
<summary>Answer</summary>
a
</details>

### Question 5
What happens when you call `.clearstamp(5)` after using `.stamp()`?  
a. The turtle's position is reset.  
b. All stamps are removed.  
c. The stamp with ID 5 is removed.  
d. The screen is cleared.

<details>
<summary>Answer</summary>
c
</details>

## Exercise
Write a Python program for drawing each of these shapes!

(Easy) Challenges 1-5: The student should be able to do all of these with the concepts learned up to this point.  

(Medium) Challenges 6-11: The same concepts can be used, but the scripts may be longer for these challenges.  

(Hard) Challenges 12-14: Advanced concepts such as loops may be needed, so do not do these challenges. They will be returned to later.

![Screenshot 2024-03-03 152334](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/05aa8e7e-2d0e-4555-88e8-be2eb9341fe4)

<details>
<summary>Hint</summary>
Attempt each challenge first. If you are stuck, you can refer to the Scripts (Answer Key) > Lesson 3 Scripts folder, where there will be a sample solution for each of the challenges (only one of the many ways that you can create each image!). This exercise is meant to boost your creativity and learn programming concepts using Turtle along the way!
</details>

<details>
<summary>Challenge 1</summary>

![Lesson 3 Challenge 1](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/8b448eae-ed37-4e43-9486-7cc0496b9eb7)
</details>

<details>
<summary>Challenge 2</summary>

![Lesson 3 Challenge 2](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/78ccaddb-ddaf-48bf-9f12-35bd3c157c70)
</details>

<details>
<summary>Challenge 3</summary>

![Lesson 3 Challenge 3](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/d35cb0f9-a9b3-4c30-a979-4ff1b91fe5fb)
</details>

<details>
<summary>Challenge 4</summary>

![Lesson 3 Challenge 4](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/6a154abe-4bf8-43eb-8cf1-1a5e54e372da)
</details>

<details>
<summary>Challenge 5</summary>

![Lesson 3 Challenge 5](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/0912f251-4405-4371-8ec1-56030fc3eab3)
</details>

<details>
<summary>Challenge 6</summary>

![Lesson 3 Challenge 6](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/1ff8faf9-e86a-427b-8608-43dc14b6d98a)
</details>

<details>
<summary>Challenge 7</summary>

![Lesson 3 Challenge 7](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/d51defa5-0080-46c7-9103-3061d30c0abf)
</details>

<details>
<summary>Challenge 8</summary>

![Lesson 3 Challenge 8](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/f2550f8d-ff56-485a-9fd2-5b795c898853)
</details>

<details>
<summary>Challenge 9</summary>

![Lesson 3 Challenge 9](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/572d1c85-b038-4247-a95e-742c8b0a23ec)
</details>

<details>
<summary>Challenge 10</summary>

![Lesson 3 Challenge 10](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/07ebf431-ce45-4c4b-ad1e-817e2713c6f9)
</details>

<details>
<summary>Challenge 11</summary>

![Lesson 3 Challenge 11](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/2f80bc20-5fe6-4e7e-af8e-4f34810c007b)
</details>

<details>
<summary>Challenge 12</summary>

![Lesson 3 Challenge 12](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/a4e2d327-49a9-4a6a-8905-ffab3ca17fa8)
</details>

<details>
<summary>Challenge 13</summary>

![Lesson 3 Challenge 13](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/6294d66a-70b9-4073-9334-1ca7fb0df8f9)
</details>

<details>
<summary>Challenge 14</summary>

![Lesson 3 Challenge 14](https://github.com/The-Logic-Coders/turtle-program/assets/97239180/d9cd89b8-ca4f-42f0-a550-f6ff1b69cf43)
</details>