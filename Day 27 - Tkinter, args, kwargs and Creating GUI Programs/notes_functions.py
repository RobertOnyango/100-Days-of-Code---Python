#### ADVANCED PYTHON ARGUMENTS ####
# Python provides the functionality of defining a function with default values as opposed to keyword arguments that will have to be passed in the function call i.e.
'''
def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c

my_function(a=2, b=1, c=3)

# FUNCTION WITH DEFAULT VALUES
def my_function(a=2, b=1, c=3):
    # Do this with a
    # Then do this with b
    # Finally do this with c

my_function()

# To change a value, we can do it in teh function call and the rest of the default values remain i.e.
my_function(b=5)
'''

'''
# Hover over the write function from the turtle class to see the default values it has i.e. move, align, font. The first argument, args, is the text we want to write. This is feature can be seen in the foo() function below
import turtle

tim = turtle.Turtle()
tim.write()
'''

'''
def foo(a, b=4, c=6): 
    print(a, b, c)
 
foo(1) # 1 4 6
'''

'''
def foo(a, b=4, c=6): 
    print(a, b, c)
 
foo(4, 9) # 4 9 6
'''

### *args: Many Postional Arguments - UNLIMITED POSITIONAL ARGUMENTS
'''
### *args: Many Postional Arguments - UNLIMITED POSITIONAL ARGUMENTS ###
def add(*args):
    for n in args:
        print(n)
# You can pass in any number of arguments
add(1, 4, 5, 66, 90, 8)
'''

# Function that takes in any number of arguments (*args) and adds them
# NOTE: *args is a tuple, hence why a loop is necessary for addition
'''
def add(*args):

    # Because args is a tuple, you can access each argument value via the index
    print(args[0]) #4

    sum=0
    # Loop through each of the arguments
    for n in args:
        sum += n
    print(sum)

add(4,6,78,1,5)
'''


# UNLIMITED KEYWORD ARGUEMENTS
# NOTE: **kwargs is a dictionary
'''
def calculate(**kwargs):
    print(kwargs) # {'add': 3, 'multiply': 5}
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"]) # 3

calculate(add=3, multiply=5) 
'''
# Function that accepts an integer value n, then proceeds to add it to three, (the value from the key 'add') and the multiplies it by 5, (the value to the key 'multiply')
'''
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
'''

# NOTE: Tk module is an extrapolation from an another language with different syntax, For it to work as it does, all Tk original arguments were taken as **kwargs

# Let's create a class with the same **kwargs arguments like Tk. **kwargs are optional arguments that are passed in when a new object is being initialized from the class
class Car:
    def __init__(self, **kwargs):
        # When you initialize the car object, you must have the make and model values otherwise the code will not run
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        # For dictionatries, you can use the get() function. The get() function will return a None if the keys i.e. make and model are not defined. This is not crash the program
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

# Initialize an object with only to keys initialized
car = Car(make="BMW", model="M340i")
print(car.model)
print(car.color) #None