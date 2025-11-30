from turtle import Turtle, Screen
import random

screen = Screen()
# Setup default Window Size
screen.setup(width=500, height=500)
# Boolean that holds race state
is_race_on = False
# Prompt user for input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Starting y_cordinate
y_cordinate = -100
# List that will hold all our turtle
all_turtles = []

# Looping through each color to get the each object
for color in colors:
    # Create an instance for each color
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    # Assign the individual color for each instance
    new_turtle.color(color)
    # Moving the turtle to the left most part of the Window using goto
    new_turtle.goto(x=-230, y=y_cordinate)
    # Increment y_cordinate after each iteration
    y_cordinate+=50
    # Add each created turtle to the turtle list
    all_turtles.append(new_turtle)

# Start race only once the yser has entered a bet
if user_bet:
    is_race_on = True

# Race
while is_race_on:
    # Loop through all the turtles in the list, moving each by a random distance
    for turtle in all_turtles:
        # Confrim if the turtle has reached the right most part of the Window i.e. at 250 (Each turtle is 40 X 40), to determine the game winner
        if turtle.xcor() > 230:
            # Stop the while loop whenever one turtle has won
            is_race_on = False
            # Extract the winner's pencolor from the color function
            winning_color = turtle.pencolor()
            # Check if user made the right bet
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # the random distance that each turtle moves by
        rand_distance = random.randint(0,10)
        # Move the turtle
        turtle.forward(rand_distance)



screen.exitonclick()