# A class Snake that will have the snakes creation, behaviour and experience

from turtle import Turtle

# Starting positions are always fixed
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# Constant we want the snaKe to move by
MOVE_DISTANCE = 20
# Set the directions
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        # Empty list to store each individual segment as one item i.e. the Snake
        self.segments = []
        
        # Call the function that will actually draw the snake
        self.create_snake()

    # Function that creates the snake
    def create_snake(self):
        # Loop through each of the first postions
        for position in STARTING_POSITIONS:
            '''
            REPLACED BY: add_segment() to perform the function of actually adding a segment to the snake
            # Create the segment
            new_segment = Turtle("square")
            # Change its color to white
            new_segment.color("white")
            # Move penup so the segment doesn't draw lines
            new_segment.penup()
            # Set it at the position according the positions we are looping towards
            new_segment.goto(position)
            # Append the segment to the segments list
            self.segments.append(new_segment)
            '''
            self.add_segment(position)

    # Function that moves the snake
    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
            # Get hold of the cordinates of the second to last positioned segment
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            # Assign the cordinates to the last segment so it moves
            self.segments[segment_number].goto(new_x, new_y)

        # Actually move the first segment
        self.segments[0].forward(MOVE_DISTANCE)

    # Functions that move the snake: Remember that Right=0 Up=90, Left=180, Down=270
    # NOTE: Due to the move function, we only need to move the first segment
    '''
    def up(self):
        # Set new heading by getting current heading and adding 90 to it
        current_heading = self.segments[0].heading()
        new_heading = current_heading + 90
        # Assign heading(direction) to segment
        self.segments[0].setheading(new_heading)
    '''
    # NOTE: Rules of snake game require that for example the snake can't move upwards then dowmnwards immediately or left then right
    def up(self):
        # Confirm that the snake is not moving downwards
        if (self.segments[0].heading() != DOWN):
            self.segments[0].setheading(UP)
    
    def down(self):
        # Confirm that the snake is not moving upwards
        if (self.segments[0].heading() != UP):
            self.segments[0].setheading(DOWN)

    def left(self):
        # Confirm that the snake is not moving rightwards
        if (self.segments[0].heading() != RIGHT):
            self.segments[0].setheading(LEFT)
    
    def right(self):
        # Confirm that the snake is not moving leftwards
        if (self.segments[0].heading() != LEFT):
            self.segments[0].setheading(RIGHT)

    # Function that adds a new segment to the snake. Accepts a position argument where we want to add the segment
    def add_segment(self, position):
        # Create the segment
        new_segment = Turtle("square")
        # Change its color to white
        new_segment.color("white")
        # Move penup so the segment doesn't draw lines
        new_segment.penup()
        # Set it at the position according the positions we are looping towards
        new_segment.goto(position)
        # Append the segment to the segments list
        self.segments.append(new_segment)

    # Function that increases the snake size
    def extend(self):
        # Get the position of the last element in the segments list and add a segment at this last elements position. Remember the move function that ensures the snake moves
        self.add_segment(self.segments[-1].position())

    # Function that resets the snake after getting high_score and game ending
    def reset(self):
        # Move each segment to a location off screen
        for segment in self.segments:
            segment.goto(1000, 1000)
        # Clear all the segments from the list
        self.segments.clear()
        # Create a new 3 segement snake
        self.create_snake()