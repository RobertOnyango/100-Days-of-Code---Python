from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    '''
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)
    
    '''
    # new_list = [new_list for item in list]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    
    shuffle(password_list)

    '''
    password = ""
    for char in password_list:
        password += char
    '''
    password = "".join(password_list)
    password_input.insert(0, password)
    # Paste password direct to clipboard
    pyperclip.copy(password)

# ----- JSON ----- #
# JavaScript Object Notation is a bunch of nested lists and dictionaries.
# in-built JSON library: write ->json.dump(), read->json.load(), update->json.update()

# Function that writes to file. 
def write_to_file(data):
    with open("data.json", "w") as file:
        # Add the user input (new_data dictionary) as the first user input
        json.dump(data, file, indent=4)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # Get the user inputs
    website_name = website_input.get()
    username = username_input.get()
    password = password_input.get()
    # New dictionary item variable that will be written into the data.json file
    new_data = {website_name.title():{
        "username": username,
        "password": password
    }}

    # Validate the fields are not empty
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You cannot submit empty fields")
    else:
        try:        
            # Open the data.json file in read mode
            with open("data.json", "r") as file:
                # READ data from json file: Load method converts the data into a dictionary
                data = json.load(file)
                # print(data) -> {'Medium': {'username': 'robert@gmail.com', 'password': 'Password1'}}
                # UPDATE the old data (that we now have as the data dictionary) with a new input by the user that stored in new_data dictionary
                data.update(new_data)
        # Catch the case where the file doesn't yet exist 
        except FileNotFoundError:
            '''
            # Open the data.json file in write mode to create it
            with open("data.json", "w") as file:
                # Add the user input (new_data dictionary) as the first user input
                json.dump(new_data, file, indent=4)
            '''
            write_to_file(new_data)
        # When there's no data in the file but it exists
        except:
            # Write the user data in the file anyway without attempting to read anything
            '''
            with open("data.json", "w") as file:
                # WRITE or SAVE the updated data dictionary to the json file and delete all the previous data
                json.dump(new_data, file, indent=4)
            '''
            write_to_file(new_data)
        # If the file exists (there are no exceptions)
        else:
            '''
            # Open the data.json file in write mode so we can write into it
            with open("data.json", "w") as file:
                # WRITE or SAVE the updated data dictionary to the json file and delete all the previous data
                json.dump(data, file, indent=4)
            '''
            write_to_file(data)
        finally:
            # Delete texts after saving
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

            # Add the focus and username back to the default state
            website_input.focus()
            username_input.insert(0, "robert@gmail.com")




# -------------------------- SEARCH FUNCTIONALITY -------------------------#

# Create the search button function
def find_password():
    # Get the website_input
    website = website_input.get()
    # what if there's no file
    try: 
        # Open the file in read mode: HANDLE FileNotFoundError
        with open("data.json", "r") as file:
            # 1. Get hold of the data from the file. Comes as a dictionary
            data = json.load(file)
    # What if there's no file at all during the first run
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found. Please add a new password")
    # What if the file exists but it is empty
    except: 
        # Pop up message indicating file is empty
        messagebox.showinfo(title="Error", message="No data in the password's file. Please add a new password")
    else:     
        website_name = website.title()
        # 2. Loop through the dictionary, checking if the keys match user input
        if website_name in data:
            messagebox.showinfo(title=f"{website_name}", message=f"Email: {data[website_name]['username']} \n Password: {data[website_name]['password']}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists")

    


# ---------------------------- UI SETUP ------------------------------- #

# Setup the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Setup the canvas
canvas = Canvas(width=200, height=200)
# Get the image
my_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(row=0, column=1)

# Website Label and Entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=17)
# Set the cursor here at program launch
website_input.focus()
website_input.grid(row=1, column=1)

# Username Label and Entry
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
# Add a starting value for the username/email
username_input.insert(0,"robert@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

# Password label, entry and generate password button
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=17)
password_input.grid(row=3, column=1)

generate_pass_button = Button(text="Generate Password", command=password_generator)
generate_pass_button.grid(row=3, column=2)

# Add password to text file button
add_password = Button(text="Add", width=30, command=save_password)
add_password.grid(row=4, column=1, columnspan=2)

# The search button that finds the password
search_button = Button(text="Search", command=find_password, width=10)
search_button.grid(row=1, column=2)


window.mainloop()

