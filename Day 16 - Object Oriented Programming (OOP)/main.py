from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1. Print the report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

coffee_maker.report()
money_machine.report()

# 2. Check resources are sufficient
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            #3. Process coins
            #4. Check if transaction is successfull
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)