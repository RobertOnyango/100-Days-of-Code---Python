from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# Global variable for current card and words to learn
current_card = {}
to_learn = {}

# --------------- READ DATA FROM FILE ---------------#

# read the data file and convert to dataframe
# df = pandas.read_csv("data/french_words.csv")
try: 
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError: 
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # Convert dataframe to a dictionary where each row is an single dictionary in the list
    to_learn = df.to_dict(orient="records")



# --------------- FUNCTION THAT CONTROLS NEXT FRENCH TEXT CARD ------------------#

def next_card():
    global current_card
    global flip_timer

    # Cancel the 3 second wait after going to a new card
    window.after_cancel(flip_timer)
    # Random dictionary from list with {French: word, English: word}
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Start count to flip card on every Frnch card
    flip_timer = window.after(3000, func=flip_card)


# --------------- FLIP CARD TO ENGLISH TEXT ----------------#

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ----------------- REMOVE LEARNT and KNOWN FRENCH WORDS FROM LIST ---------------#

def is_known():
    # Remove current card dictionary from the list of dictionaries
    to_learn.remove(current_card)
    # create a new dataframe from list
    data = pandas.DataFrame(to_learn)
    # store the dataframe as a csv. These are the words user is yet to learn
    data.to_csv("data/words_to_learn.csv", index=False)
    # call next card
    next_card()


# --------------- UI -------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer that will determine when to flip card
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.grid(row=0,column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Call teh function so the text is read on first run
next_card()

window.mainloop()