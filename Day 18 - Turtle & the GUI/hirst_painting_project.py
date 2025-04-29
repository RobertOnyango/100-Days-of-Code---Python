# import colorgram
import turtle as turtle_module
import random

# rgb_colors = []
# # Extract colors from the image
# colors = colorgram.extract('image2.png', 80)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors) # These colors will be added to the color_list below

# Have the color module change it's colormode to 255 for RGD
turtle_module.colormode(255)

color_list = [(230, 232, 236), (235, 231, 233), (223, 232, 226), (208, 160, 82), (56, 89, 131), (145, 91, 40), (139, 26, 49), (221, 207, 106), (134, 176, 202), (157, 46, 85), (45, 55, 104), (168, 160, 39), (129, 189, 144), (83, 20, 45), (186, 92, 105), (39, 42, 66), (189, 140, 167), (85, 125, 182), (58, 39, 31), (79, 153, 164), (88, 157, 92), (195, 79, 73), (45, 74, 77), (81, 74, 43), (161, 201, 218), (58, 131, 128), (216, 175, 187), (170, 206, 172), (179, 189, 211), (219, 182, 169), (48, 73, 73), (148, 39, 36), (48, 65, 64)]

# Use the color list above to draw a spot painting
# Program requirments: Draw 10 X 10 rows of spots. Dots should be 20 in size and the spaces should be 50

# Create a turtle object
tim = turtle_module.Turtle()
tim.speed("fastest")

# We are drawing dots, we need to get rid of the lines
tim.penup()

#Hide turtle
tim.hideturtle()

# Change the arrow position on the screen
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
# Variable holding the number of dots we want to draw
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # Draw the dot
    tim.dot(20, random.choice(color_list))
    # Tim to move forward by 20
    tim.forward(50)

    # If we've drawn 10, 20, 30.... dots, move above to new starting position
    if dot_count % 10 == 0:
        # Move the turtle above the current row, the to the leftmost (above the original starting position)
        tim.setheading(90) # Turn left (Look up)
        tim.forward(50) # Move up by 50
        tim.setheading(180) # Turn left
        tim.forward(500) # Move to the starting position
        tim.setheading(0) # turn left


#Create screen object from turtle module
screen =  turtle_module.Screen()
screen.exitonclick()

