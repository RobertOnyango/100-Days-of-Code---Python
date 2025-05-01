# Food class that the snakes eats and grows. Once food is eaten, another food item appears somewhere else at random
# Food obejct will be from trutle so the Food class will inherit from the turtle class
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        # Call the Turtle class init() method and initialize it
        super().__init__()
        self.shape("circle")
        self.penup()
        # Make the food size 10 X 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # Food object should go to a reandom X, Y location when first initialized
        self.refresh()
    
    # Fucntion that refreshes the foods position
    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)