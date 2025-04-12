#********** FUNCTIONS WITH INPUTS ***********#
# Function definition with parameter declared
def greet(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")
    print(f"{name}, Isn't the weather nice?")

# Function call with argument passed
greet("Robert")


def life_in_weeks(age):
    weeks = (90 - age) * 52
    print(f"You have {weeks} weeks left")

current_age = int(input("How old are you?"))

life_in_weeks(current_age)

#********** POSITIONAL VS KEYWORD ARGUMENTS **********#

# Function declaration with two parameters
def greet_with(name, location):
    print(f"Hello {name}. \nWhat is it like in {location}.")

# Positional Arguments: Position of parameters = Position of arguments
greet_with("Robert", "Nowhere")

# Keyword arguments
def greet(name, location):
    print(f"Hello {name}. \nWhat is it like in {location}.")

# Keyword argument implicitly associated to parameter
greet(location="Everywhere", name="Tabby")

# Love Score Calculator
def calculate_love_score(name1, name2):
    love = "love"
    true = "true"
    love_number = 0
    true_number = 0

    combined_name = (name1 + name2).lower()
    for char in combined_name:
        if char in love:
            love_number += 1

    for char in true:
        if char in combined_name:
            true_number += 1

    love_score =  str(true_number) + str(love_number)
    print(f"Love Score = {love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")
