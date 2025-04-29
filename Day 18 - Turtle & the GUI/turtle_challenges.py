#********** PYTHON TURTLE **********#
#Turtle Graphics - Allows us to make changes to the UI
# To figure out how to work with the Turtle module, take a look at its documentation i.e. via Google and StackOverflow

# import turtle
# tom = turtle.Turtle()

# from turtle import Turtle, Screen

# Aliasing a module
import turtle as t
# terry = t.Turtle()

# from turtle import * # From the turtle module, import everything(*)
import random

tim = t.Turtle()

# Change shape of to turtle
# tim.shape("turtle")

#Change the color of the turtle
# tim.color("red")

#Tk Color specification string (tkinter). Can be used to create a GUI in Python. (https://cs111.wellesley.edu/reference/colors)
# tim.color("gray50")

# ***** TURTLE CHALLENGE 1 ******

# Move the turtle: Draw a Square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# Draw a Sqaure using for loop
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# ****** TURTLE CHALLENGE 2 ******

#  Draw a Dashed Line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# ****** TURTLE CHALLENGE 3 ******

# #  Draw a triangle, square , pentangon, hexagon, heptagon, octagon, nonagon and decagon (360 / no. of sides)
# colors = ["red", "green", "yellow", "blue", "orange", "grey", "purple"]
# # Function that return the shape
# def draw_shape(num_sides):
#     # Get the angle
#     angle = 360 / num_sides
#     # Draw the shapes
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# # Loop through the numbers 3 to 10 to get the number of sides in each shape and call the draw_shape function to draw each shape
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# ****** TURTLE CHALLENGE 4 ******
# # Generate a random walk
# colors = ["red", "green", "yellow", "blue", "orange", "grey", "purple"]

# # The directions the turtle can move
# directions = [0, 90, 180, 270]

# # Increase pensize
# tim.pensize(10)

# # Speed up the animation
# tim.speed("fastest")

# for _ in range(200):
#     # Genrate random color in each movement
#     tim.color(random.choice(colors))
#     # Move the turtle forward by 30 paces
#     tim.forward(30)
#     # Set the movement direction to be random
#     tim.setheading(random.choice(directions))


# PYTHON TUPLES DATATYPE AND GENERATING RANDOM RGD COLORS
# Python tuple example
# Unlike a list, you can't change the elements in a tuple i.e. Immutable.
# USE CASES: Constant list, Color scheme for websites.
# my_tuple = (1, 3, 8)

# # Items are indexed
# print(my_tuple[1]) #3

# # To change contents of a tuple, put the tuple in a list to convert it to a list
# print(list(my_tuple)) #[1, 3, 8]


# CHALLENGE 4: With random colors generated and using a tuple
# Generate a random walk

# Tap into the actual turtle module and not the object
# t.colormode(255)

# # Create a random color
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     # Return a tuple
#     return (r, g, b)

# # The directions the turtle can move
# directions = [0, 90, 180, 270]

# # Increase pensize
# tim.pensize(10)

# # Speed up the animation
# tim.speed("fastest")

# for _ in range(200):
#     # Genrate random color in each movement
#     tim.color(random_color())
#     # Move the turtle forward by 30 paces
#     tim.forward(30)
#     # Set the movement direction to be random
#     tim.setheading(random.choice(directions))


# CHALLENGE 5: Draw a Spirograph
# Tap into the actual turtle module and not the object
t.colormode(255)

# Function to create a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Return a tuple
    return (r, g, b)

# Speed up the animation
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    # 360 degree is a the angle of a full circle
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        #Draw a circle
        tim.circle(100)
        #Get current heading
        current_heading = tim.heading()
        #Set new heading
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()