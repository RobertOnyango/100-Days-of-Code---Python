#********** OBJECT STATE AND INSTANCES **********#
# Object Instance: Different objects from the same Class. Each object can have different attributes and methods i.e. Objects are with different States.

# Python Code that simulates a race between turtles where the user places a bet on who the winner will be at the end.
from turtle import Turtle, Screen
import random

screen = Screen()
# Set screen dimension: Width of screen makes the start (left pane) and finish (right pane) of the race.
screen.setup(height=400, width=500)

#Popup where the user will input bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

# Colors of our turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# List the turtles on the left axis
y_positions = [-100, -70, -40, -10, 20, 50, 80]

# Array to hold the turtles 
all_turtles = []

# Variable to hold the race state
is_race_on = False

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    # Remove line
    new_turtle.penup()
    new_turtle.color(colors[index])
    # Move turtle object to the left most position of our pance
    new_turtle.goto(x=-230, y=y_positions[index])

    # Each new created turtle appended to list
    all_turtles.append(new_turtle)

# Confirm a user has placed a bet
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # Detect when the turtle has reached the 230 mark. I f we detect for 250, the turtle would have already overshone the screen i.e. 250 - (40 / 2) = 230. Using 40 because the turtle object is 40 X 40.
        if turtle.xcor() > 230:
            is_race_on = False
            # Get the pen color of the winning turtle
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else: 
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # Set the random distance to move each turtle
        random_distance = random.randint(0, 10)
        # Move each turtle forward at a different pace
        turtle.forward(random_distance)
    


screen.exitonclick()