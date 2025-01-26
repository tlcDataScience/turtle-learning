# Lesson 10: Project - Turtle Race

## Learning Objectives
- Build a game by applying the concepts learned in Lessons 1-5
- Learn how to create a basic user interface for the game, including displaying messages
- Develop problem-solving skills by debugging issues that arise during the development of the game, such as turtles not moving as expected or the game not responding to user input

## Project Brief
In this project, you will be creating a two-player Turtle Race using Turtle Graphics.
- **Description:** In the game, the players take turns rolling a die to move their turtles the specified number of steps forward.
- **Objective:** The goal is to have your turtle reach home base before your opponent's turtle does.
- **Game End:** The game ends when one of the players reaches home base.
- Any messages generated in this game will be printed in the Terminal.

## Steps for Game Development

### Game Environment
1. Import the `turtle` and `random` libraries. More information on the `random` library will be discussed in Lesson 11. For now, you will only use `random.choice()` to return a random number from 1-6 for each dice roll.

```python
import turtle
import random
```

2. Copy and paste the applicable lines of code from Template.py (Scripts (Answer Key) > Lesson 0 Scripts).

### Game Setup

*Player 1 turtle*
1. Create a turtle for Player 1.
2. Specify the color and shape of the turtle.
3. Specify the turtle's starting location without drawing anything yet (`(-200, 100)`).

*Player 2 turtle*
1. Create a turtle for Player 2 that is a clone of the turtle for Player 1.
2. Specify a different turtle color to be able to tell the difference between Player 1 and Player 2.
3. Specify the turtle's starting location without drawing anything yet (`(-200, -100)`).

*Player 1 home base*
1. Move the turtle to `(300, 60)`.
2. Start drawing with the turtle.
3. Draw a circular home base of radius 40.
4. Return the turtle to its starting location without drawing anything yet (`(-200, 100)`).

*Player 2 home base*
1. Move the turtle to `(300, -140)`.
2. Start drawing with the turtle.
3. Draw a circular home base of radius 40.
4. Return the turtle to its starting location without drawing anything yet (`(-200, -100)`).

<details>
<summary>Hint</summary>
Use <code>my_turtle.penup()</code> and <code>my_turtle.pendown()</code>
</details>

### Main Gameplay

*Die roll and turtle movement*
1. Trigger die rolls by getting user input.
2. Randomly generate a die roll using `random.choice([1, 2, 3, 4, 5, 6])`.
3. Print the result of the die roll.
4. Move the corresponding turtle forward the specified number of steps (you can multiply the die roll by a number, say 20, to move the turtles by larger distances for faster gameplay).

*Winning condition*
1. Check if Player 1 has won (reached `(300, 100)`).
2. Check if Player 2 has won (reached `(300, -100)`).
3. If either player has won, print which player won the game.
4. Terminate the program.

<details>
<summary>Hint</summary>
Combine a for loop and conditional statements.
</details>

### Optional
You can make a third turtle to show an on-screen message of who wins the game at the end.

### Debugging Tips
- While testing your game, there may be times you see an issue that you want to fix right away before your code is finished executing. You can press the "Stop" button (gray square in the trinket.io top menu) for this.
- Understand what may have gone wrong by reading the error message in the Terminal. It may give a clue to the line number/s that have issues.
- Check if all of your variable names are consistent. Variables names are case-sensitive, so errors here will cause issues in running the code.
- Check your code indentation levels (`Tab` to shift inwards, `Shift + Tab` to shift outwards). You may have accidentally moved something to the wrong place.
- As always, you may reference the Scripts (Answer Key) > Lesson 10 Scripts folder in this repository if all of the above are not working.

## Demo
Run your game and ensure that everything is working properly!