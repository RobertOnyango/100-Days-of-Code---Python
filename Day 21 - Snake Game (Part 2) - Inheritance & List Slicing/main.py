from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
# Create the food item
food = Food()
# Create the scoreboard item
scoreboard = Scoreboard()

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

    # TODO 4: DETECT COLLISION WITH SNAKE FOOD
    # Detect when snake comes into contact with food using the distance() from the Turtle class i.e. Compare the distance from the first segment of the snake to the food object considering the sizes of each.
    # If segments collide:
    if snake.segments[0].distance(food) < 15:
        # print("Collided with food")
        # Food object refreshes to a new location
        food.refresh()
        # Extend the snake
        snake.extend()
        # TODO 5: CREATE A SCOREBOARD
        scoreboard.increase_score()
    
    # TODO 6: DETECT COLLISION WITH WALL
    # If snake has gone too far to the right or too far to the left or too fat to the top or too far to the bottom
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        # End Game
        game_is_on = False
        scoreboard.game_over()

    # TODO 7: DETECT COLLISION WITH TAIL
    # If head collides with any segment in the tail, trigger game over function
    # [1:] slice the segments from after the first segment
    for segment in snake.segments[1:]:
        # if segment == snake.segments[0]:
        #     pass
        # elif snake.segments[0].distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
