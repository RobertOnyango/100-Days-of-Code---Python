from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Get the user inputs
    website_name = website_input.get()
    username = username_input.get()
    password = password_input.get()

    # Validate the fields are not empty
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You cannot submit empty fields")
    else:
        # A message box that the user uses to confirm the entries from the messagebox code
        is_ok = messagebox.askokcancel(title={website_name}, message=f"These are the details entered: \n Email: {username} \n Password={password} \n Is it okay to save?")

        if is_ok == True:
            # Open data.txt file
            with open("data.txt", "a") as file:
                # Add the inputs to a data.txt file
                file.write(f"{website_name} | {username} | {password}\n")

            # Delete texts after saving
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

            # Add the focus and username back to the default state
            website_input.focus()
            username_input.insert(0, "robert@gmail.com")
    

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

website_input = Entry(width=35)
# Set the cursor here at program launch
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

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


window.mainloop()

