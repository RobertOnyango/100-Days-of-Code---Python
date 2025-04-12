#********** A program that illustrates a text-based calculator **********#
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(first_number, second_number, operator):
    if operator == "+":
        solution = add(first_number, second_number)
        print(f"{first_number} + {second_number} = {solution}")
        return solution

    if operator == "-":
        solution = subtract(first_number, second_number)
        print(f"{first_number} - {second_number} = {solution}")
        return solution

    if operator == "*":
        solution = multiply(first_number, second_number)
        print(f"{first_number} * {second_number} = {solution}")
        return solution

    if operator == "/":
        solution = divide(first_number, second_number)
        print(f"{first_number} / {second_number} = {solution}")
        return solution

print(art.logo)

# Variable to hold first number
num1 = float(input("What's the first number?: "))
accumulate_result = True

while accumulate_result:
    print("+ \n- \n* \n/")

    #Pick the operation
    operation = input("Pick an operation: ")

    # Variable to hold the next number
    num2 = float(input("What's the next number?: "))

    # Variable to hold returned result
    result = calculator(first_number=num1, second_number=num2, operator=operation)

    status = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

    if status == "y":
        num1 = result
    elif status == "n":
        accumulate_result = False



