##### TKINTER INTRODUCTION ######

# Import Tkinter module for GUI
# import tkinter
from tkinter import *

# Create a new window
# window = tkinter.Tk()
window = Tk()

# Give the window a title
window.title("My first GUI program")

# Window size
window.minsize(width=500, height=300)

# Create components to put in window:

# Label Component
# my_label = tkinter.Label()
my_label = Label(text="I am a label", font=("Arial", 24, "bold")) # Using tkinter, we first create a label as so and then we specify how the component will be laid out on screen

# Use the pack() that will get hold of the component and centre it in on the screen
my_label.pack()
# Various Parker method arguments
# my_label.pack(side="left")
# my_label.pack(expand=True)

# To change the text from my_label
my_label["text"] = "New text" #As dictionary (See **kwargs in notes_functions)
my_label.config(text="New text") # Using config() -> Similar to get() in classes with **kwargs attributes. Can be used to edit multiple attributes.

# Event listener for the button
def button_clicked():
    print("I got clicked")
    # Get hold of the value input in the field (Entry Component)
    user_input = input.get()
    # Challenge: Show the "Button got clicked" on my_label when button gets' clicked: Key=text
    my_label["text"] = user_input
    # OR
    # my_label.config(text="Button got clicked")

# Button Component
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry Component
input = Entry(width=10)
input.pack()




# While loop that keeps the window in the screen
window.mainloop()