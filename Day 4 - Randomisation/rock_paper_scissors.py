#********** ROCK, PAPER & SCISSORS **********#
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Store the game options in a list
options_list = [rock, paper, scissors]

#Store the length of the list
list_size = len(options_list)

#prompt the user to enter an input
user_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Make sure the user selected an appropriate input not greater than list
if user_index > list_size - 1:
    print("You typed an invalid number. You lose!")
else:
    # Assign the index to get an element from the list
    user_choice = options_list[user_index]

    # Print user choice
    print(user_choice)

    # Let the computer choose a random choice from the list of variables
    computer_choice = random.choice(options_list)
    print(f"Computer chose: \n {computer_choice}")

    # Rules of the game
    # Rock beats scissors
    if user_choice == rock and computer_choice == scissors:
        print("You win")
    elif computer_choice == rock and user_choice == scissors:
        print("You lose")
    # Paper beats rock
    elif user_choice == paper and computer_choice == rock:
        print("You win")
    elif computer_choice == paper and user_choice == rock:
        print("You lose")
    # Scissors beats paper
    elif user_choice == scissors and computer_choice == paper:
        print("You win")
    elif computer_choice == scissors and user_choice == paper:
        print("You lose")
    # All other options i.e. same symbols selected
    else:
        print("You draw")
