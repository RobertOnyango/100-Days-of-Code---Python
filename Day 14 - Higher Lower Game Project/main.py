# A game that compares who has more followers on instagram
# Data is as a list of dictionaries with details of each option in each
import random
from game_data import data

# Extract each item from the dictionaries into actionable data
# print(data[1]["name"])


USER_SCORE = 0

# Function that formats data from teh dictionary into a workable format
def format_dictionary(choice):
    choice_name = choice["name"]
    choice_description = choice["description"]
    choice_country = choice["country"]

    return(f"{choice_name}, a {choice_description}, from {choice_country}.")

# Function that compares which dictionary has more followers
# Arguments: User Guess, Choice A followers and Choice B Followers
# Returns: Whether the user got the option right
def correct_guess(user_guess, choice_1, choice_2):
    if choice_1 > choice_2:
        if user_guess == "a":
            return True
    else:
        if user_guess == "b":
            return True

# Variable that controls the game state
game_should_continue = True
# Pick a random dictionaries from the dataset: use random.choice
# Picking choice_b because it will be assigned to choice_a on every iteration and a new random picked for choice_b
choice_b = random.choice(data)

while game_should_continue:
    # Assign choice b to choice a
    choice_a = choice_b
    # Generate a new random choice for choice b
    choice_b = random.choice(data)

    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Compare A: {format_dictionary(choice_a)}")

    print("vs")

    print(f"Against B: {format_dictionary(choice_b)}")

    # Prompt user to select with has more followers between the two dictionaries i.e. key=follower_count
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get followers for each choice
    choice_a_followers = choice_a["follower_count"]
    choice_b_followers = choice_b["follower_count"]

    # Compare the which dictionary has more followers
    is_correct = correct_guess(user_answer, choice_a_followers, choice_b_followers)

    if is_correct:
        USER_SCORE += 1
        print(f"You're right! Current score {USER_SCORE}")
    else:
        print(f"Sorry, that's wrong. Final score: {USER_SCORE}.")
        game_should_continue = False