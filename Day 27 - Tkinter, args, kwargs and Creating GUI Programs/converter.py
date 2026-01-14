# Program that convertes Miles to Km.

from tkinter import *

FONT = ("Arial", 12, "normal")

# Function that converts Miles to Km.
def conversion():
    # Get the user input and covert it to a float
    input = user_input.get()
    float_input = float(input)

    # Multiply that input by 1.60934 to get its value in km
    new_value = float_input * 1.60934

    # Round off the input to 2 decimal places, feed it to the result
    result_label.config(text=round(new_value, 2))
    

# Setup the Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=50, pady=50)

# input(entry) component
user_input = Entry(width=15)
user_input.grid(row=0, column=1)

# miles label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

# is_equal_to label
is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(row=1, column=0)

# result label
result_label = Label(text=0, font=FONT)
result_label.grid(row=1, column=1)

# km label
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

# calculate buttom
calculate_button = Button(text="Calculate", command=conversion)
calculate_button.grid(row=3, column=1)

# While loop that keeps the window in the screen
window.mainloop()