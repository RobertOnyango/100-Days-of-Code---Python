# A program that generates the name of a user's band from answered prompts

# Welcome message
print ("Welcome to the name Band Generator!")

# User prompt to ask them of the  city
print("Which city did you grow up in?")

# Store user input in variable 'city'
city = input()

# User prompt two. Ask the prompt and store in variable 'pet_name' on same line
pet_name = input("What's the name of your pet?\n")

# Print name of band combining the two inputs
print("The name of your band is " + city + " " + pet_name)