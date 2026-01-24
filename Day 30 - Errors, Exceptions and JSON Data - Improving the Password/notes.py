#----- HANDLING ERRORS & EXCEPTIONS ------#

# Try to open a non-existent file: FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-exitent_key"]

#IndexError: Reading an item from a non-existent index in the list
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#----- Catching Exceptions -----#
# We can catch the above exceptions so that the errors cause more gracefull failures since we can determine what happens after a failure
'''
KEYWORDS and FORMAT
try: A block of code that if run might cause an exception

except: Do this if there was an exception

else: Do this if there no exceptions

finally: Do this no matter what happens. Normally used for cleaning this up after code execution
'''

# Example of opening a non-existence file that will cause a FileNotFoundError
'''
try:
    file = open("a_file.txt")
except:
    # If file does not exist, simply create it then open it
    file = open("a_file.txt", "a")
    file.write("Do something")
'''


'''
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
    print(a_dictionary["non-existent_key"])

except FileNotFoundError:
    # If file does not exist, simply create it then open it
    # NOTE: Only using an except block on its own, the code will ignore all errors even those not accounted for. For example, the try block tries to print a non-existent ky value. Without any modification, the KeyError will be ignored in the console. To fix it, specify the type of error you want to excempt i.e. FileNotFoundError

    file = open("a_file.txt", "a")
    file.write("Do something")

# You can have multiple exceptions. For this one get the specific key that is causing the error from the errormessage
except KeyError as error_message:
    print(f"{error_message} does not exist")

# Runs only if there are no exceptions (non at all) thrown in the try block
else:
    content = file.read()
    print(content)

# Code that runs no matter what happens
finally:
    file.close()
    print("File was closed.")
    # ----- RAISING YOUR OWN EXPECTIONS ----- #
    # Keyword: raise -  Useful when you want to raise an exceptino no matter what happens in the code blocks above
    # raise KeyError
    raise TypeError("This is an error that I made up.")

'''

# When would we want to raise our own custom exceptions?
# The code below calculate the BMI, we would raise an exception if the user enters an unrealistic height i.e. above 3 meters
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human heigh cannot exceed 3 meters")

bmi = weight / height ** 2
print(bmi)


