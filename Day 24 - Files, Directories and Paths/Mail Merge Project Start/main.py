#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Variable list to hold the names
list_of_names = []

# Extract the names from the list of names into a list
with open("./Input/Names/invited_names.txt", mode="r") as name_file:
    # Use the readlines() method to extract each line as a list item and assign it to our variable
    list_of_names = name_file.readlines()

# Loop through each name from the list
for current_name in list_of_names:
    # Use the strip method to remove the \n (New Line symbol) to get just the name
    name = current_name.strip("\n")

    # Read the contents of the template letter into a variable
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        template = letter.read()

    # Use the replace() function to replace the [name] with the current name in the loop
    new_letter = template.replace("[name]", name)

    # Save the new letter in the ReadyToSend folder with the required name
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(new_letter)