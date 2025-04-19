# A program that simulates a Coffee Machine Operations

# Menu options for the coffee machine
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

# Global variable to hold profit
PROFIT = 0
# Initial resources in the coffee machine to begin with
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function that takes in resources used and user input to print report
def print_report():
    global PROFIT
    resources["money"] = PROFIT
    for key in resources:
        print(f"{key.capitalize()}: {resources[key]}")

# Fucntion that accepts order ingrdients and compares them with the resources in machine. Return True if order can continue, False if otherwise
def resource_checker(order_ingredients):
    for item in order_ingredients:
        # The keys of the two dictionaries have to match for this if statement to run
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there's not enough {item}")
            return False
        print(order_ingredients)
        return True

# Function that prompts user for the coins he/she has and calculates then returns the total. 
def process_coins():
    print(f"Please insert coins.")
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))

    total_cost = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

    return total_cost

# Function that takes in the cost of the drink from the dictionary and the total amount entered by the customer and compares them.
def transaction_successfull(order_cost, amount_paid):
    global PROFIT
    if amount_paid >= order_cost:
        # Return change
        change = round(amount_paid - order_cost, 2)
        print(f"Here is ${change} in change")
        # Add money to as profit to the machine resources
        PROFIT += order_cost
        return True
    else:
        print(f"Sorry that's not enough monery. Money refunded")
        return False
    
# FUnction that accepts the customer order and order_ingredients then reduces the ingredient count in the resources
def make_drink(order_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order_name}. Enjoy!")

# Variable that holds machine state to ON
machine_on = True

while machine_on:
    # TODO 1: Prompt user for coffee option (take_orders function)
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    # TODO 2: Turn off the machine by entering "off" to the prompt
    # Check if input is off during order stage
    if user_input == "off":
        print("MACHINE OFF")
        #Turn machine state to off
        machine_on = False
    # TODO 3: Print report when user enters "report" to the prompt
    elif user_input == "report":
        print_report()
    else:
        # Variable to hold the customer's drink dictionary with the ingredients and cost
        drink = MENU[user_input]

        # TODO 4: Check if the resources for the drink is sufficient. Function returns True, so order continues. Assign TRUE value from fuction to order variable
        order = resource_checker(drink["ingredients"])

        # Variable to hold the cost of the drink
        cost = drink["cost"]

        # TODO 5: Process coins is sufficient resources: Prompt user to insert coins and calculate total monetary value of coins (coin_calculator function)
        if order:
            coins_inserted = process_coins()
            print(coins_inserted)
            # TODO 6: Check transaction successful? i.e. Enough money inserted for the drink? If no, refund the money. If yes, cost of drink added to machine and should reflect on "report" prompt. Machine should also offer change (transaction_processor function)
            if transaction_successfull(order_cost=cost, amount_paid=coins_inserted):
                # TODO 7: Make coffee
                make_drink(order_name=user_input, order_ingredients=drink["ingredients"])




