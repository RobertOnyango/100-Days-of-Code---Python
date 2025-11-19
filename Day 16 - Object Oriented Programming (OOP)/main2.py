from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize objects from the class
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    # Prompt user for drink choice
    choice = input(f"What would you like? {menu.get_items()}").lower()

    # Process the input i.e. Check for MENU item or OFF or report
    if choice == "off":
        print("MACHINE OFF!")
        machine_on = False
    elif choice == "report": # Show current resource allocations at machine start time
        coffee_maker.report()
    else:
        # Select the dictionary from the menu where the user input(choice) is the key and assign it to variable
        drink = menu.find_drink(choice)
        # Confirm that the resources are sufficient for the item selected by user
        if coffee_maker.is_resource_sufficient(drink):
            # Process the payments & Confirm that the transaction was successfull
            if money_machine.make_payment(drink.cost):
                # Make coffee
                coffee_maker.make_coffee(drink)
