########## STRING MANIPULATION ##########
print("Hello" + " Robert") # spaces are very important in python: Indentation errors

########## INPUTS ##########
# Take note of the execution sequence of the functions
# Ctrl + / makes a whole line of code into a comment
print("Hello " + input("What is your name?") + "!") 

########## VARIABLES ##########
# Assign user prompt to variable name
name = input("What is your name?")
# Print the variable
print(name)

name2 = "Robert"
print(name2) #Robert

name2 = "Angela"
print(name2) #Angela

#Get string length use len()
print(len(input("What is your name?")))

username = input("What is your name?")
length = str(len(username)) # You can only concatenate strings not integers.
print("Your name is " + username + " and it has " + length + " characters.")

