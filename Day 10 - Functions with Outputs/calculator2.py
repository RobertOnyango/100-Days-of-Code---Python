#********** A program that illustrates a text-based calculator **********#
import art

# TODO: Write out the 4 functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add the 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# TODO: Use the dictionary operations to perform the calculations
# print(operations["*"](4,8))

# Function to carry out the calculations
def calculator():
    print(art.logo)
    accumulate_result = True
    # Variable to hold first number
    num1 = float(input("What's the first number?: "))
    # Run the calculation at least once, then repetitively unless prompted by the user
    while accumulate_result:
        # Always print the keys(operation symbols) after the first number is captured
        for symbol in operations:
            print(symbol)
        # Prompt user for an operation to perform and store in a variable
        operation_symbol = input("Pick an operation: ")
        # Prompt user for second input
        num2 = float(input("What is the next number?: "))
        # Call the operation functions based on the operation symbol input: Operation symbol = Keys for our dictionary
        answer = operations[operation_symbol](num1, num2)
        # Print out the results of the operation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        # If user wants to continue calculations, answer is initial round of while loop will become num1
        if choice == "y":
            num1 = answer
        # If user does not want to continue while loop, exit it by negating the looping condition
        else:
            accumulate_result = False
            print("\n" * 20)
            calculator()
# Call the calculate function
calculator()
