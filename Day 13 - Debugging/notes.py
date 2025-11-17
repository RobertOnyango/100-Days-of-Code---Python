#********** DEBUGGING **********#
# OPTION 1: Describe the problem

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? Loops through the numbers 1-20
# 2. When is the function meant to print "You got it"? When the loop is at the final number 20
# 3. What are your assumptions about the value of i? i will definitely reach 20

# Problem: i never reaches 20: Fix is range(1, 21)



# OPTION 2: Reproduce the bug: When does the error actually happen

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

# Reproduce error print(dice_num) where dice_num = 6.
# The array indexes are 0 - 5, so dice_images[6] is out of range i.e. IndexError
# FIX: dice_num = randint(0, 5)



# OPTION 3: Play Computer
# If I were a computer, how would I execute this code?
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# BUG: Input 1994 doesn't print anything.
# REASON: 1994 not captured in any if statement block
# FIX: year <= 1994 in 1st if block or year => 1994 in 2nd if block.



# OPTION 4: Fix the Errors in the Editor or console
# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")

# BUG 1: print statement expects an indent
# BUG 2: age cannot accept input string e.g. twelve i.e. ValueError: invalid literal for int() with base 10: 'twelve'
# Copy error message for Bug 2 in console and search in Google
# REASON: int cannot accept input that is not a number of type string
# FIX: try...catch block
# Catch the error instead of stopping the program and catching it

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")


# OPTION 5: Print is Your Friend
word_per_page = 0
pages = int(input("Number of pages: "))
print(f"pages: {pages}")
word_per_page = int(input("Number of words per page: "))
print(f"words_per_page: {word_per_page}")
total_words = pages * word_per_page
print(total_words)


# OPTION 6: Use a Debugger: The Pycharm Debugger
# Other online debuggers include:
# Pythontutor.com
# Thonny Editor

import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        # BUG: The list was not being updated in each iteration, only the last iteration where it updates the last item after the loop
        # FIX: Add the append() to the for loop by using an indent
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Using the debugger in Pycharm:
# 1. Define a breakpoint in the gutter of your editor i.e. the numbers on the left of your editor. Breakpoint puts a break on your code on that line
# 2. Go to debug run mode to open the debug console and see the buttons.
# 3. Step Over Button: Executes code line by line stopping at the next line. The highlighted line is the one executing next and the one above is the one just executed
# 4. Step Into Button: Will execute line by line but when it encounters a module (code in another file e.g. random.randint()), will go into the definition of the function and show you the function works
# 5. Step Out Button: Step out of Step Into.
# 6. Step Into My Code: Step into code in files written by us, in our local file directory and opens it in debug mode

# Console: Shows what is to be printed during our code execution
