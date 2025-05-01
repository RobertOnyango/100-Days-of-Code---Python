# SEE day20notes.py FOR MORE DETAILS ON THE METHODS BELOW

# Class that handles the creation of the snake object:
# Attributes: Method that creates the snake itself as 3 segments into one
# Methods: Method that moves the snake, preceding segment takes the position of current segment as 1st segment takes new position forward, hence movement
from turtle import Turtle

'''
INSTRUCTOR RECOMMENDED CONSTANTS
 To allow easire game modification of the game using the 2 metrics. Otherwise I had them as:
self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
and 
20
''' 
# Snake starting positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Default move distance
MOVE_DISTANCE = 20
# Set DIRECTIONS
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        # Will store the 3 segments as one item
        self.segments = []

        # Method that will be called when snake object os initialized and called to draw the snake
        self.draw_snake()
    
    # Funtion to draw the three segments
    def draw_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Function that gives position to add new segment
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        # TODO2: Remove line
        new_segment.penup()
        new_segment.goto(position)
        # TODO2: Way of treating and working with the segments as they're one as a list
        self.segments.append(new_segment)
    
    # Funtion that adds a new segment to the snake
    def extend(self):
        # Get hold of the last segment in list and grab its position then add new segment in the same position as the last segment
        self.add_segment(self.segments[-1].position())

    # Function to move the segemts
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get hold of the cordintates of segment 2
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Move segment 3 to segment 2 position 
            self.segments[seg_num].goto(new_x, new_y)
        
        # Move the first forward i.e. segment one leading with the direction
        self.segments[0].forward(MOVE_DISTANCE)

    # Function to move the snake upwards
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    # Function to move the snake downwards
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    # Function to move the snake left
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    # Function to move the snake right
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)


