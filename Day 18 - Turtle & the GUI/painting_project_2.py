'''
import colorgram

# Variable to hold the extracted colors
colors = colorgram.extract('image2.png', 50)
# List hold the extracted colors in RGB
color_list = []
# Extract the colors from the image
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_list.append((r, g, b))

print(color_list)
'''

import turtle as t
import random

color_list = [(1, 10, 30), (229, 235, 242), (239, 232, 238), (122, 95, 41), (71, 31, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 171), (151, 92, 115), (35, 90, 26), (7, 154, 72), (205, 63, 91), (221, 178, 218), (168, 129, 77), (1, 64, 147), (3, 79, 29), (4, 220, 218), (80, 135, 179), (132, 158, 177), (81, 110, 136), (116, 187, 164), (11, 215, 222), (117, 19, 37), (131, 224, 209), (230, 173, 165), (243, 205, 7), (70, 72, 44), (186, 190, 199), (91, 48, 43), (128, 223, 230)]


# TODO: A painting with 10 by 10 rows of spots. Each spot should be around 20 in size and spaced by 50
t.colormode(255)

# Create the Turtle object tim
tim = t.Turtle()

# Function that draws a complete horizontal line of dots
def draw_horizontal_dots():
    for _ in range(10):
        # Draw a dot, assign it a random color
        tim.dot(20, random.choice(color_list))
        # Specifiy the space
        tim.penup()
        tim.forward(50)
        tim.pendown

# Function that moves the pointer upwards
def move_upwards():
    # Return pointer back to start of the current line
    tim.penup()
    tim.backward(500)
    # Move the pointer upwards by turning it 90 degrees (face upwards) and moving it by 50 spaces
    tim.setheading(90)
    tim.forward(50)
    # Reset the direction of the pointer to face the left
    tim.setheading(0)
    tim.pendown()

# Move the pointer faster
tim.speed("fastest")

# Set the starting position so that we can clearly see in the Window
tim.penup()
tim.goto(-120, -120)
tim.pendown()

# Disappear the turtle
tim.hideturtle()

# We want 10 lines drawn, so we have 10 iterations
for _ in range(10):
    draw_horizontal_dots()
    move_upwards()

screen = t.Screen()
screen.exitonclick()