#************ NAMESPACES AND SCOPE ************#
# Namespace: Global and Local scope applies to variables, functions etc.
# Nesting does not matter for global variables but be wary of indentation in local variables and functions

# Global variable
enemies = 1

def increase_enemies():
    # Local Scope
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies() # Enemies inside function 2
print(f"enemies outside function: {enemies}") # Enemies outside funtion 1

# Global Scope: Variable defined outside functions and is available for use in all functions
player_health = 10

# Local Scope: Exists within functions. Portion_strength can't be accessed outside the drink_portion function
def drink_portion():
    portion_strength = 2
    print(portion_strength)
    print(player_health)

drink_portion() # 2  # 10

#********** BLOCK SCOPE **********#
# There is no Block scope in Python

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) # Skeleton

game_level = 3
enemies_list = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies_list[0]

    print(new_enemy)

create_enemy() #Skeleton

# print(new_enemy) # NAMEERROR: name new_enemy is not defined as it is in a local

#********** GLOBAL VARIABLES **********#
# Modifying Global Scope

# Global Variable
enemies = 1

# def increase_enemies():
#     # To tap into global variable defined outside the local scope of this function
#     global enemies
#     # Proceed to modify the variable: Complete independent of when you created.
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# NOTE: Avoid modifying global scope in functions as in the example above

# Function to increase the global variable enemies
def increase_enemies(enemy):
    return enemy + 1

# Call function, add enemies as parameter and return sum
enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

#********** GLOBAL CONSTANTS **********#
# Variables defines that you never want to change ever again in your code
# Naming convention: Upper Case, separated by underscores
PI = 3.14159
GOOGLE_URL = "https://www.google.com"
