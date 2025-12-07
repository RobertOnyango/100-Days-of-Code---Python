# A python program allowing a user to play the snake game
from turtle import Screen
import time # Help to slow the screen updates down
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setup the screen of the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn off the tracer so we determine when the screen should update to avoid the lagging look when turtle does it automatically (TODO 2)
screen.tracer(0)

# TODO 1: Create a snake body: Create 3 squares on teh screen lined up against each other
# NOTE: Each square turtle is 20 X 20. Every new turtle is created at position (0,0)

'''
REPLACED BY SNAKE CLASS: Setting up the variables of the class

# Starting positions are always fixed
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Empty list to store each individual segment as one item i.e. the Snake
segments = []
'''


# Variable that maintains game state
game_is_on = True

'''
REPLACED BY SNAKE CLASS: Calling the create_snake method in the Snake class as part of the initialization of the class

# Loop through each of the first postions
for position in starting_positions:
    # Create the segment
    new_segment = Turtle("square")
    # Change its color to white
    new_segment.color("white")
    # Move penup so the segment doesn't draw lines
    new_segment.penup()
    # Set it at the position according the positions we are looping towards
    new_segment.goto(position)
    # Append the segment to the segments list
    segments.append(new_segment)

'''
# Create the snake object
snake = Snake()
# Initialize the food object
food = Food()
# Initialize the scoreboard object
scoreboard = ScoreBoard()

# Setting up screen listners (TODO 3)
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# TODO 2: Move the snake continuously forward, we tell it to change direction
# NOTE: Use a while loop because we want the snake to contiously move forward
while game_is_on:
    # Update the screen here (See screen.tracer(0) function). Placing it here means the screen will only update after all the segments have moved forward
    screen.update()

    # Slow the screen updates down: Add a 0.1 second delay
    time.sleep(0.1)
    
    # NOTE: Moving the snake forward by moving each segment forward will not satisfy the game condition. We need, counting from the last segment, that it moves to the succeding segments position, subsequently throughout the snakes body, as the user only changes the direction of the first segment
    
    # for segment_number in range(start = 2, stop = 0, step =-1): 
    # Think of the segments array where the first segment is at the postion 0 of the segments array, but we want to start the loop from the last segment going backwards
    '''
    REPLACED BY SNAKE CLASS: The move method

    for segment_number in range(len(segments)-1, 0, -1):
        # Get hold of the cordinates of the second to last positioned segment
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        # Assign the cordinates to the last segment so it moves
        segments[segment_number].goto(new_x, new_y)

    # Actually move the first segment
    segments[0].forward(20)
    '''
    # Call the move() method from the Snake class
    snake.move()

    # TODO 3: Control the snake using keyboard controls (Direction keys)

    # TODO 4: Detect collision with food such that when the snake hits the food, a new piece of food is created randomly at a diffenet location
    # Using the distance() method from turtle module where by we compare the distance from snake head to the food object(that we put in parenthesis) 
    # NOTE: Food is 10x10 and Snake head is 20x20, 15 is a good number to use
    if snake.segments[0].distance(food) < 15:
        # Food should go to new random location
        food.refresh()
        # Snake size should increase
        snake.extend()
        # TODO 5: Create a scoreboard: When snake hits food, score updated
        scoreboard.increase_scores()

    # End Game = Game over should be shown on the screen and the snake should no longer move
    # TODO 6: End Game case 1 - Detect collision of the snake with a wall
    # If snake head has gone too far to the right (> 280) or has hone too far to the left (< 280) or has gone too far up (> 280) or has gone too far down (< -280)
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        # Reset snake
        snake.reset()

    # TODO 7: End Game Case 2 - Detect collsion of the snake with tail (Head hits any part of its body)
    '''
    for segment in snake.segments:
        # Check that cuurent segment is not the snake head. If it is, pass
        if segment == snake.segments[0]:
            pass
        # If head collides with any segment in tail, game over
        elif snake.segments[0].distance(segment) < 10:
            # End game
            game_is_on = False
            # Show scoreboard
            scoreboard.game_over()
    '''
    
    for segment in snake.segments[1:]:
        # If head collides with any segment in tail, game over
        if snake.segments[0].distance(segment) < 10:
            # Show new scoreboard
            scoreboard.reset()
            # Get new snake
            snake.reset()

screen.exitonclick()