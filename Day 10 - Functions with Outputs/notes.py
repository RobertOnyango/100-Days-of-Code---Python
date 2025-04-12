#*********** FUNCTIONS WITH OUTPUTS **********#
def  function():
    return 3 * 2 # Return Key word

output = function()
print(output)

# Function that converts the inputs to Title Case
def format_name(f_name, l_name):
    # Title() has an output
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name(f_name="ROBERT", l_name="onyango")
print(formatted_string)
# print(format_name(f_name="ROBERT", l_name="onyango"))

# Take note of the difference between Return and Print
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

# Output of function_1 becomes the input of funct[ion_2. Make use of the Return Keyword
output = function_2(function_1("hello"))
print(output)

#********** MULTIPLE RETURN VALUES **********#
# Return makes the end of a function: Code after return will not be executed
# You can have multiple return values in a function
# You can have empty return values without anything after wards

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        # return Ends the program here due to no inputs
        return "You did not provide a valid input" # You can add error messages
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))

#*********** DOCSTRINGS **********#
# A way for us to create documentation as we code
# Goes as the first line after the function interaction
# Syntax: 3 quotation marks
# Shows up on the function call
def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



