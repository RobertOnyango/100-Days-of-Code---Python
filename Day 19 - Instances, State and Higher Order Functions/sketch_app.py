# Etch-a-sketch App using Turtle() classs
# Keys: W = Forwards, S = Backwards, A = Counter-Clockwise, D = Clockwise, C = ClearDrwawing

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Screen to listen to key strokes
screen.listen()

# Move forwards function
def move_forwards():
    tim.forward(20)
screen.onkey(key="w", fun=move_forwards)

# Move backwards
def move_backwards():
    tim.backward(20)
screen.onkey(key="s", fun=move_backwards)

# Counter Clockwise (Turn Left)
def move_counter_clockwise():
    # Get new heading from current heading
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
screen.onkey(key="a", fun=move_counter_clockwise)

# Move clockwise (Turn Right)
# NOTE the difference between the two functions counter_clockwise and clockwise, two different ways of achieving the same goal
def move_clockwise():
    tim.right(10)
screen.onkey(key="d", fun=move_clockwise)

# Clear screen
def clear():
    tim.clear()
    # Penup
    tim.penup()
    # Reset turtle position
    tim.home()
    tim.pendown()
screen.onkey(key="c", fun=clear)

screen.exitonclick()
