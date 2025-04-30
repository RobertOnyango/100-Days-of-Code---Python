from turtle import Screen
from snake import Snake
import time

# Setup the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO 1: CREATE A SNAKE BODY
# Create the snake object
snake = Snake()

# TODO 3: CONTROL THE SNAKE MOVEMENTS
# Listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Variable that holds game state
game_is_on = True

# TODO 2: MOVE THE SNAKE AUTOMATICALLY
while game_is_on:
    screen.update()
    # Screen will update every 0.1 second
    time.sleep(0.1)

    snake.move()
