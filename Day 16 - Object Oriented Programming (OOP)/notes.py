#********** OBJECT ORIENTED PROGRAMMING - OOP **********
# Procedural Programming: Functions do each thing as the code runs from top to bottom, jumping into a function as required: See Day 1 - 15

# OOP: Allows reusable to code samples to different programs, sometimes in different contexts e.g. naviagition module of a self-drive car might be useful in an autonomous drone

# HOW TO USE OOP: CLASSES AND OBJECTS
'''
An object must have two features:
1. What it has -> Attributes i.e. variables
2. What it does -> Methods i.e. functions

You can have multiple objects from the same object type i.e. Multiple objects from a Class
'''

# CONSTRUCTING OBJECTS AND ACCESSING THEIR ATTRIBUTES AND METHODS
'''
Class is written in Pascal Case e.g. CarBlueprint()

Create a car object from the class CarBlueprint i.e.
car = CarBlueprint()
'''

# Create an object from a class that is already created by someone else i.e. class turtle. Note here that turtle is the module (file created by another dev) and within this module there is a class named Turtle()

# import turtle

# # Construct the object called timmy from the class Turtle in the file turtle. Parenthesis() constructs/initializes the object created from the class.
# timmy = turtle.Turtle()

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy) # <turtle.Turtle object at 0x0000025FC330C2F0>
timmy.shape("turtle")
timmy.color("brown2")
timmy.forward(100)

# OBJECT ATTRIBUTES e.g. car.speed: car = object, speed = attribute
myscreen = Screen()
print(myscreen.canvheight)

# OBJECT METHODS e.g. car.stop(): car = object, stop() = method
myscreen.exitonclick()

# HOW TO ADD PYTHON PACKAGES AND USE PYPI(Python Package Index)
# Python Packages: A file that achieves a specific goal, normally written with a lot of files by a lot of people

#prettytable = Package, PrettyTable = Class in package
# from prettytable import PrettyTable

# table = PrettyTable()

# # Methods
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# #Attributes
# table.align = "l"

# print(table)

