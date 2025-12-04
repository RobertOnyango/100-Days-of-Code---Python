# TODO 2&3:A Paddle Class whose objects will be the Player's tools in the game of Ping Pong. Inherits from the Turtle class so we have all the methods from the turtle class.
# The paddle xtics: width = 20, height = 100, x_pos = 350, y_pos = 0. On-click -> Up arrow key = Move up and Down arrow key = Move Down

from turtle import Turtle

class Paddle(Turtle):
    # Accepts a position argument which should be a tuple (x,y) coordinates
    def __init__(self, position):
        super().__init__()

        # Set the size, color and postion
        self.color("white")
        self.shape("square")
        # NOTE: All turtle objects start with a 20x20 size. So the numbers below are a factor to which we multiply the size to get the shape we want
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    # Function that moves the paddle up
    def go_up(self):
        # Only the y position is changing so get the current y_cord and add a figure to it
        new_y = self.ycor() + 20
        # Move to current x_cor but new y_cor
        self.goto(self.xcor(), new_y)
        
    # Function that move the paddle down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)