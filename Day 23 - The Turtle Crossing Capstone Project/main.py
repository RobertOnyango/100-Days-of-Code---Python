# A Python prograsm of the Turtle crossimng game

'''
How the game play works:
1. A turtle moves forward when you press the "Up" key. It can only move forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
4. When the turtle collides with a car, it's game over and everything stops.
'''

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO 1: Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
# Create turtle object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Setup screen to listen for key events
screen.listen()
screen.onkey(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    # TODO 2: Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs.
    # Create a car on every screen refresh (0.1s)
    car_manager.create_car()
    # Move each car on every refresh
    car_manager.move_car()

    # TODO 3: Detect when the turtle player collides with a car and stop the game if this happens.
    # Loop through all the cars in the car_manager all_cars list
    for car in car_manager.all_cars:
        # Compare the distance between the player turtle and each car
        if car.distance(player) < 20:
            # Stop the game
            game_is_on = False
            # Input game over text
            scoreboard.game_over()

    # TODO 4: Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
    if player.is_at_finish_line():
        # Reset the turtle
        player.reset()
        # Increase the game speed
        car_manager.increase_game_speed()

        #  TODO 5: Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.
        
        # Update level in scoreboard
        scoreboard.increase_level()


screen.exitonclick()

    
