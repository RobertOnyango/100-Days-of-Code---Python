import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
# tim.color("red")

# TODO 1: Draw a Square using the Turtle module
# Turtle moves forward by 100: Forward = Turtle is facing East by default 
# tim.forward(100)
# Turtle turns and faces the South = Makes a 90 degree turn on its right side
# tim.right(90)

# The above two comments shows the default directions that the turtle makes. This can be a loop of instructions, using the square's 4 sides as the range
'''
for _ in range(4):
    tim.forward(100)
    tim.right(90)
'''

# TODO 2: Draw a Dashed Line
'''
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
'''

# TODO 3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon. Each shape will be drawn by a random color. Each side of each shape will have the size of 100. All teh shapes will be overlayed on each other.
# NOTE: Side count = 3-10. To know the angle of the turn is (360-Number_of_sides_of_each_shape)
'''
# Variable to hold the number of sides: Start with 3 since first shape is a triangle
num_of_sides = 3

# List of colors to satisfy the requirement that each shape needs to have a different color
colors = ["red", "green", "yellow", "blue", "orange", "grey", "purple"]

# The number of sides needs to increment after each iteration but stop at 10
while num_of_sides < 11:
    tim.color(random.choice(colors))
    # The number of sides also decides the for loop for each shape
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(360 / num_of_sides)
    
    # Increment the number of sides by one after each shape is drawn by the for loop
    num_of_sides += 1
'''

# TODO 4: Draw a random walk - Move in a random direction between North, East, South or West, Progressing each time by the same distance, using a different color. The Lines are a bit thicker than before and the turtle moves a bit faster

# Define the 4 directions i.e. where does the turtle face before moving. Consider that a full circle is 360 degrees.
# NOTE: From the docs, use setheading() function. North=0, East=90, South=180, West=270. But in my setup, East=0, North=90, West=180, South=270

'''
# List to hold the directions
directions = [0, 90, 180, 270]

# List to hold the colors
colors = ["red", "green", "yellow", "blue", "orange", "grey", "purple"]

# Increase pensize width
tim.pensize(10)

# Increase speed of the turtle
tim.speed(10)

for _ in range(100):
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colors))
    tim.forward(25)
'''

'''
# Change the colormode of the turtle module to accept 255 instead of strings
t.colormode(255)

# Function that returns a tuple of random colors in r,g,b
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)

# List to hold the directions
directions = [0, 90, 180, 270]

# Increase pensize width
tim.pensize(10)

# Increase speed of the turtle
tim.speed(10)

for _ in range(100):
    tim.setheading(random.choice(directions))
    tim.color(random_color())
    tim.forward(25)
'''

# TODO 5: Draw a Spirograph: Have turtle draw a number of circles each with a radius of 100. Each circle should have a different random color. Spirograph = For each circle to be drawn, the tilt has to be changed by a little bit
t.colormode(255)
tim.speed("fastest")

# Function that randomizes the colors using RGB
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

# Function that accepts the difference (in degrees) between each circle as a parameter and proceeds to draw the circles, using this argument/param as the value to shift the heading of the pen drawing
def draw_spirograph(size_of_gap):
    # 360 degree is a the angle of a full circle, dividing it by the difference in degrees will ensure that the Spirograph is complete perfectly
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        #Draw a circle
        tim.circle(100)
        #Get current heading in degrees
        current_heading = tim.heading()
        #Set new heading
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()