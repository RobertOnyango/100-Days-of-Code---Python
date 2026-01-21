# A Pythin program that simulates the Promodo Clock where the user works intensly for 25 minutes then gets a 5 minute break recursively for three rounds. Then a final 25 minute session followed by a 20 minute break. The clock resets to the initial state after this 20 minute break.

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.25
# Variable that holds the total number of reps. Last rep is 8.
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# Function that resets all the texts (labels), stops the timer, resets the timer to 00:00 and resets the REPS to 0
def reset_timer():
    global timer, REPS
    # Stop the timer 
    window.after_cancel(timer)
    # Reset timer text
    canvas.itemconfig(timer_text, text="00:00")
    # Reset timer label
    title_label.config(text="Timer", fg=GREEN)
    # Reset check_marks
    checkmarks.config(text="")
    # Reset the REPS to 0
    REPS = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
# TODO 4: Tie the count_down function to the Start button
def start_timer():
    global REPS
    # Start timer, immediately increment the reps count
    REPS += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    
    # The last rep has the value of 0
    if REPS % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    # All the even number of reps are breaks
    elif REPS % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    # All the odd number of reps are working minutes 
    else: 
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)
   



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# The Event Driven nature of the program (via window.mainloop()) does not allow us to use another loop here as it will not reach the mainloop(). If we try, the program will not run

# Count_down function that provides the loop functionality. When called, the after() calls the function and on each iteration reduces the count by 1
def count_down(count):
    # Edit the timer output to read in munutes and seconds as opposed to the seconds
    count_minute = math.floor(count / 60)
    count_seconds = count % 60

    # When the count is fully divisible by 60, count_seconds is 0 instead of the desired 00. The following code would fix this but notice, we are checking the value of an int for the variable but assigning it a char without any errors.
    '''
    Dynamic Typing in Python - You can change the data type of a variable by simply changing the contents of the variable
    '''
    # single_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # if count_seconds == 0:
    #     count_seconds = "00"
    # elif count_seconds in single_values:
    #     count_seconds = f"0{count_seconds}"

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # TODO 3: Change the Timer text in the canvas
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    # TODO 2: Ensure the count down does not go to the negative int
    if count > 0:
        global timer
        # TODO 1: Timing widget - after() that waits for a duration in ms after which call the function setup, You can pass the parameters (positional arguments) as you need.
        timer = window.after(1000, count_down, count - 1)
    # TODO 5: Call start_timer() function once the count goes to zero signalling the end of each rep
    else: 
        start_timer()
        # For every two reps, we add a checkmark to the check_mark label. A work_session is the complete of WORK+REST cycle, so we divide REPS by 2
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✓"
        
        # Update the checkmarks label
        checkmarks.config(text=marks)
         
  

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Label
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Canvas widget allows us to add images on top of each other. Width and heigh values are in pixels
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# A photoimage class that reads a file and get's hold of the image stored therein
tomato_img = PhotoImage(file="tomato.png")
# Define x and y positions the image in the canvas and the image
canvas.create_image(100, 112, image=tomato_img)
# Add some text for the timer and assign it to a variable which will be used in the count_down()
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Checkmark Lable
checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(row=2, column=1)

# Stop button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()