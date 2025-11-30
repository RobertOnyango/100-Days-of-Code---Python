# A Food Class that renders itself on screen as a blue spot. Everytime the snake touches it, this food class object moves to a different random location
# NOTE: The object will be continously created so long as the snake touches it and the while the game is still live

from turtle import Turtle
import random

# The Food class will inherit attributes from the Turtle class i.e. Turtle is the Superclass for the Food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Call the shape method from the Turtle Class
        self.shape("circle")
        # As the food object moves, we don't want it to draw lines
        self.penup()
        # Reduce the shapesize
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # Change the color of the food object
        self.color("blue")
        # Increase speed of creation
        self.speed("fastest")
        # Call refresh button
        self.refresh()     

    # Function that randomly selects a position for our food object to be in. Used once a food object is hit by the snake head
    def refresh(self):
        # Generate random integers that will guide the random positions of the food object on screen. Remeber the screen size is 300 x 300, we don't want a food object to appear right in the Edge of the screen, our Snake object wouldn't get to it
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # Tell food to go random (x,y) position
        self.goto(random_x, random_y)
        