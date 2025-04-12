import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
# Condition for game
game_over = False
#List to hold correct letters
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        # If guessed letter matches a letter in word, add to display and correct letters
        if letter == guess:
            display += letter
            correct_letters.append(letter) #Add the correct letter to a list with correct letters already input
        #  Letter in the chosen letters list is not the letter currently being looped through
        elif letter in correct_letters:
            display += letter
        # If guessed letter doesn't match a work in letter, add _ to display
        else:
            display += "_"

    print(display)

    # If the display still has _, game not over. While loop exist.
    if "_" not in display:
        game_over = True
        print("You win.")
