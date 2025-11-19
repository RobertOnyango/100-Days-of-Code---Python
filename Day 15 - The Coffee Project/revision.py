# A program that simualtes a vendor Coffee Machine Program

# Menu options for our coffee machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100, 
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Global variable to hold the profit
profit = 0

# Initial resource allocation on the machine
resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
}

# Function that processes user input
def process_user_input(user_input):
    valid_inputs = ["espresso", "latte", "cappuccino", "report", "off"]
    if user_input in valid_inputs:
        return user_input
    else:
        print("Incorrect value!")
        return False
        

# Function that confirms whether the ingredients are sufficient to make the order. Function Arguments: Order ingredients from the MENU/customer order and compares with the resources i.e. This function argument will be the ingredients dictionary
def are_resources_sufficient(order_ingredients): # {'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
    for item in order_ingredients:
        # item = water, milk, coffee
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there wasn't enough {item}")
            return False
    return True

# Function that calculates the coins input by the user
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# Function that takes teh arguments: Money_received = The coins processed by the process_coins() function and the cost of the drink from the cost dictionary in each MENU item.
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # Refer to the global 'profit' variable by using the keyword global
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function that takes the drink name for the output printout and the ingredients such that we subtract the order inngredients from the total resources (machine ingredients) from the resource ingredient
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Boolean that holds whether machine is on or off
machine_on = True

while machine_on: 
    # Process user inputs: "espresso/latte/cappuccino" or the secret word for admins "off" to turn off machine, or "report" to see the report
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()

    # Confirm that the choice has been input correctly
    if process_user_input(choice):
        if choice == "off":
            print("MACHINE OFF!")
            machine_on = False
        elif choice == "report": # Show current resource allocations at machine start time
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: {profit}")
        else:
            # The user by entering the name of the drink automatically selects a dictionary item
            drink = MENU[choice] # Example latte -> {'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
            # Confirm that resources are sufficient once drinks are ordered: Pass the ingredients from the order to the function
            if are_resources_sufficient(drink["ingredients"]):
                # Process coins(vending machine)
                payment = process_coins()
                # Confirm transaction was successfull
                if is_transaction_successful(payment, drink["cost"]):
                    # Make coffee
                    make_coffee(choice, drink["ingredients"])
