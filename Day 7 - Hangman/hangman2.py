import random
word_list = ["aardvark", "baboon", "camel"]

# Pick a word from the list randomly and store it in variable chosen_word
chosen_word = random.choice(word_list)
print(chosen_word)

# Variable to hold the dashes "_" as they would appear on screen to a user
placeholder = ""

# Variale to store the length of the chosen word to set for loop bounds
word_length = len(chosen_word)

# Loop through each letter in the chosen_word and replace with the dashes, making use of the placeholder variable
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Prompt user to guess a letter
guess = input("Guess a letter: ").lower()

# Variable that holds the game state i.e. letter guesses
display = ""

# Loop through each letter in the chosen_word and confirm if the letter guessed matches the current letter in the loop
for letter in chosen_word:
    # If letter in chosen_word matches with guess, add the letter to the display variable
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
