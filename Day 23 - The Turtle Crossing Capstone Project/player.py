# A Player class that is the Turtle the user will be controlling to cross the road

from turtle import Turtle

# Starting position of the turtle on screen
STARTING_POSITION = (0, -280)
# How much distance the turtle should move onkey press
MOVE_DISTANCE = 10
# The finish line of the turtle in y-axis
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Set the turtle shape
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        # Initially set the turtle to starting position
        self.reset()

    # FUnction that sets the turtle positions
    def reset(self):
        self.goto(STARTING_POSITION)

    # Fuction that moves the turtle forward
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Function that detects if turtle is at finish line
    def is_at_finish_line(self):
        # Get the turtles y_position and compare to the finishing line
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

        
