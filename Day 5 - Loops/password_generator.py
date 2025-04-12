# A program that generates a random password from the three lists
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#SOLUTION 1: Prints out the password with a pattern (letters,numbers,symbols)
# # Variable to store the new password
# password = ""
#
# # Loop through the letters list using the number of characters input by the user as the range
# for char in range(0, nr_letters):
#     # Randomly select the characters: For each loop, randomly select a letter and add to the password character
#     password += random.choice(letters)
#
# # Loop through the numbers list
# for num in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# # Loop through symbols list
# for sym in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# print(password)

#SOLUTION 2: Randomly select the characters for the password
# List to store the generated password
password_list = []

# Loop through the letters list using the number of characters input by the user as the range
for char in range(0, nr_letters):
    # password_list += random.choice(letters)
    password_list.append(random.choice(letters))

# Loop through the numbers list
for num in range(0, nr_numbers):
    password_list += random.choice(numbers)

# Loop through symbols list
for sym in range(0, nr_symbols):
    # password_list += random.choice(symbols)
    password_list.append(random.choice(symbols))

print(password_list) # List with letters, numbers and symbols, each as a character
# Reorder a list using the random.shuffle()
random.shuffle(password_list)
print(password_list)

# Variable to hold the password
password = ""

# Turn list to string
for char in password_list:
    password += char

print(f"Your new password is: {password}")


