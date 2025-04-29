#********** PYTHON HIGHER ORDER FUNCTIONS & EVENT LISTENERS *********#
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

# Listen to key strokes
screen.listen()

# Pass key stroke and function to onkey function. 
'''
NOTE: When you pass a function as a argument(input) to another function, you don't add the parenthesis(), you only pass the function name. The parenthesis cause the function to trigger then and there.
In our case below, we want the function onkey() to call the function move_forwards() only when the space bar is pressed.
'''
# Higher Order Function: A function that takes another function as an input and then calls the function and works with it in its body.
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()