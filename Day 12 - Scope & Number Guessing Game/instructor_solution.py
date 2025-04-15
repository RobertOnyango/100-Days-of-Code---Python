#********* NUMBER GUESSING PROJECT **********#
'''
A project that prompts the user to correctly guess a random generated number by the computer
The game will give the user guides whether their guesses are higher or lower than the random number.
The game has 2 levels:
    Easy = User gets 10 guess attempts and 9 hints
    Hard = User gets 5 guess attempts and 4 hints
'''

import random
from art import logo

# Set global variables for easy and hard levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check player's guess with computer guess
def check_answer(user_guess, actual_number, lives):
    if user_guess > actual_number:
        print("Too high")
        return lives - 1
    elif user_guess < actual_number:
        print("Too low")
        return lives - 1
    else:
        print(f"You got it! The answer was {actual_number}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Game function
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100")
    # Computer randomly picks a number between 1 and 100
    computer_answer = random.randint(1,100)

    # Prompt user to set a difficulty level: easy or hard
    turns = set_difficulty()

    while turns != 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Prompt user to make a guess and store guess in variable.
        guess = int(input("Make a guess: "))

        # Confirm if guess is right or wrong and reduce life as necessary
        turns = check_answer(user_guess = guess, actual_number = computer_answer, lives = turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != computer_answer:
            print("Guess again.")

game()