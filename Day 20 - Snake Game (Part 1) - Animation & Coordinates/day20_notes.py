from turtle import Screen, Turtle
import time

# Setup the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turs off the screen i.e. will not update screen with the code below untill we call update
screen.tracer(0)

# TODO 1: CREATE A SNAKE BODY
'''
New turtle dimensions = 20 X 20 pixels
'''
# # Define X and Y positions
# x_cordinates = 0
# # Move each snake to a x postion behind the preceeding 
# for _ in range(3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.goto(x=x_cordinates, y=0)
#     # Increment x_cordiantes by 20 (turtle object size)
#     x_cordinates -= 20

# INSTRUCTOR SOLUTION
# Define starting positions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Will store the 3 segments as one item
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    # TODO2: Remove line
    new_segment.penup()
    new_segment.goto(position)
    # TODO2: Way of treating and working with the segments as they're one as a list
    segments.append(new_segment)

# TODO 2: MOVE THE SNAKE AUTOMATICALLY: Snake continously moves forward

# Variable that holds game state
game_is_on = True

while game_is_on:
    # Call update function after the segemnts have already been created, and after each of teh segments have moved forward. Give it the illusion that teh segments are moving as one piece
    screen.update()
    # Delay time: Works with update function above
    time.sleep(0.1)

    '''
    To get the right and synced movement of our segments as one item, we need to ensure that for example segment 3 takes the place of segment 2, segment 2 take place of segment 1 and segment 1 leads with the movement direction. (Counting segments from right to left)
    '''
    # Loop through the segments from the last segment to the last
    '''
    NOTE: We're removing the keywords from the range() function for the code to run in python. See the example below for the code logice,
    for seg_num in range(start=2, stop=0, step=-1)
    for seg_num in range(start=len(segments) - 1, stop=0, step=-1)
    '''
    for seg_num in range(len(segments) - 1, 0, -1):
        # Get hold of the cordintates of segment 2
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        # Move segment 3 to segment 2 position 
        segments[seg_num].goto(new_x, new_y)
    
    # Move the first forward i.e. segment one leading with the direction
    segments[0].forward(20)

# PROCEED TO CREATE THE SNAKE CLASS WITH TODO 2 & TODO 3 ATTRIBUTES AND METHODS
















screen.exitonclick()