import turtle
import pandas

# Create the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

FONT = ("Courier", 8, "normal")

# import the image file
image = "blank_states_img.gif"
# add teh image to the shape so we can use it in turtle
screen.addshape(image)

# Call the image as the shape
turtle.shape(image)

'''
CODE THAT IS USED TO COORELATE THE DATA 50_states.csv data file AND MOUSE CLICKS IN PANDA
# Function that returns the cordinates of where the mouse has been clicked
def get_mouse_click_coor(x, y):
    print(x, y)

# Call turtle event listener for when the mouse clicks on window at the desired cordinates
turtle.onscreenclick(get_mouse_click_coor)

# Don't close window after mouse clicks
turtle.mainloop()
'''

# TODO: Confirm that the user's answer (All caps cases accounted for) matches where the user has clicked. If the user has guessed correctly, the state name is written on the map. Then the number of correct states identified is incremented. If not all correct states are selected by the user or teh user types a wrong state, the dialogue box pops up again.

# Prompt user for the input i.e. a state and store in variable
# answer_state = screen.textinput(title="Guess the state", prompt="What's another states name?")

pointer = turtle.Turtle()

# Read the csv file using pandas
data = pandas.read_csv("50_states.csv")
# Extract the state_names and add to a list
state_names = data["state"].to_list()
# Empty list that will hold all the guessed state names
guessed_states = []

# TODO 4:  Use a loop to allow the user to keep guessing
# Use the number of guesses states for the while loop 
while len(guessed_states) < 50:
    # TODO 6: Keep track of the score
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?")

    # TODO 1: Convert the answer to title_case
    answer_state_title_case = answer_state.title()

    # TODO 7: EXTRA VIDEO CODE: Saving the States Data into a CSV file to show which states we missed
    # End the game condition
    if answer_state_title_case == "Exit":
        # TODO 8: Save the missed states in a separate CSV
        # Compare the guessed_states array to the state_names array via looping through the state_names then save the items not in guessed_states array into a new array
        # NOTE: This should only be done after the game has ended i.e. After EXIT.
        # Empty array to hold the missed states
        missed_states = []
        for state in state_names:
            if state not in guessed_states:
                # Add the missing state to the array
                missed_states.append(state)

        # Create a dataframe
        new_data = pandas.DataFrame(missed_states)
        # Use the dataframe to create the new file
        new_data.to_csv("states_to_learn.csv")
        break

    # TODO 2: Check if guess is among 50 states
    # Confirm that the state name is in the list
    if answer_state_title_case in state_names:
        # Read the correct row from the csv data file
        current_state = data[data["state"] == answer_state_title_case]
        # TODO 5: Record the correct guesses in a list
        guessed_states.append(answer_state_title_case)
        # TODO 3: Write correct guesses onto the map
        # Read the x, y cordinates from the
        x_cordinate = current_state.x.iloc[0]
        y_cordinate = current_state.y.iloc[0]
        print(x_cordinate)
        # Move the turtle to the correct position according the csv data
        pointer.hideturtle()
        pointer.penup()
        pointer.goto(x_cordinate, y_cordinate)
        # Write the state name as text on map
        pointer.write(answer_state_title_case)

    


