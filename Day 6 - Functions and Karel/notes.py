#********** FUNCTIONS **********#
# Built-in functions e.g. len(), print()
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# User defined function
def my_function():
    print("Hello")
    print("Bye")

# Function call
my_function()

#********** INDENTATION **********#
# 4 spaces are preferred

#********** WHILE LOOP **********#
# While something is true, do something
number_of_hurdles = 6

while number_of_hurdles > 0:
    number_of_hurdles -= 1
    print(number_of_hurdles)

# For Loops: When you iterate over something and you need do something with each thing you're iterating over
# While Loops: When you don't care about the iterated items, you want to run a condition you want to run until a condition is met

# Reborg Hurdle 3:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left() # Face up
#     move() # Move up
#     turn_right() # Face right
#     move() # Move right
#     turn_right() # Face down
#     move() # Move down
#     turn_left() # Face Left
#
# while at_goal() != True:
#     if wall_in_front() == False: # No wall, move forward
#         move()
#     else: # Wall: Jump
#         jump()

# Reborg Hurdle 4:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()  # Face up
#     while wall_on_right() == True:
#         move()
#
#     turn_right()
#     move()
#     turn_right()
#
#     while front_is_clear() == True:
#         move()
#
#     turn_left()
#
#
# while at_goal() != True:
#     if front_is_clear() == True:
#         move()
#     else:
#         jump()

#REBORG'S WORLD MAZE
# Turn right
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while at_goal() != True
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()