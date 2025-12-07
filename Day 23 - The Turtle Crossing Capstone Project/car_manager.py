# A CarManager class that generates all the random cars and moves them across the screen

from turtle import Turtle
import random

# List of colors for the random cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# How much each car should move on each refresh
STARTING_MOVE_DISTANCE = 5
# How much MOVE_DISTANCE should increase each time the user levels up
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # Empty list that will hold all the new cars
        self.all_cars = []
        # Attribute to hold the car speed
        self.car_speed = STARTING_MOVE_DISTANCE

    # Function to create a new car. Will be called upon every screen refresh
    def create_car(self):
        # Pick a random number between one and six 
        random_chance = random.randint(1, 6)
        # Only create a car if the random number is 1, remeber the function is called on every screen refresh (0.1s)
        if random_chance == 1:
            # Create the new car from the turtle class and set its shape to square
            new_car = Turtle("square")
            new_car.penup()
            # Set the shape to default size of 20x40
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            # Select a random color for the cars
            new_car.color(random.choice(COLORS))
            # The Y-position should be random, from 250 to -250
            y_position = random.randint(-250, 250)
            new_car.goto(x=300, y=y_position)
            # Add the new car to the list of new cars
            self.all_cars.append(new_car)

    # Fucntion to move the cars
    def move_car(self):
        # Loop through list of all cars
        for car in self.all_cars:
            # Move towards the left
            car.backward(self.car_speed)

    # Function that increases the speed of the cars
    def increase_game_speed(self):
        self.car_speed += MOVE_INCREMENT

