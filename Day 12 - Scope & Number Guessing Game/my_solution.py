import random

from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100")

# Computer randomly picks a number between 1 and 100
computer_number = random.randint(1, 100)
print(computer_number)

# Prompt user to choose a difficulty level: easy or hard
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Global Variable to hold game_lives
game_lives = 0

# Insert difficulty condition game rule:
if difficulty == "easy":
    game_lives = 10
elif difficulty == "hard":
    game_lives = 5
else:
    game_lives = 0

# Prompt user to make a guess and store guess in variable.
# Function returns the user guest as int

while game_lives != 0:
    user_guess = int(input(f"You have {game_lives} attempts remaining to guess the number. "
                               f"\nMake a guess: "))

    # Decrease the lives per guess if the guess are not correct
    if user_guess > computer_number:
        print("Too high. \nGuess again. ")
        new_lives = game_lives - 1
    elif user_guess < computer_number:
        print("Too low. \nGuess again. ")
        new_lives = game_lives - 1
    else:
        print(f"You got it. The answer is {computer_number}")

    # Condition for maintaining game play with number of lives
    if new_lives == 0:
        print("You're out of lives. You lose.")
    else: 
        print("Guess again")