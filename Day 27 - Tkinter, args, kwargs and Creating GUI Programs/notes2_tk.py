# Defining the layout of each component using PACK, PLACE and GRID

# Pack orders the widget in a logical order i.e. as the code is written. You can change this using the 'side' attribute

# Place = Precise positioning via x,y values. Is too specific thus can cause problems with the increasing number of widgets

# Grid = Imagine that your window is a grid that you can divide to the number of squares in the rows and coulmns that you'd wish. It is relative to other widgets. 

# NOTE: You cannopt use Grid and Pack in the same program.

from tkinter import *

def button_clicked():
    print("Button Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Set up the Window
window = Tk()
window.title("My second GUI program")
window.minsize(width=500, height=300)
# Add padding to all the widgets in the Window
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
# my_label.pack()
# my_label.place(x=0, y=0)
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
# Add padding around the label widget
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)

#Challenge: Create a new button at a defined position
button2 = Button(text="New button")
button2.grid(column=2, row=0)


# While loop that keeps the window in the screen
window.mainloop()