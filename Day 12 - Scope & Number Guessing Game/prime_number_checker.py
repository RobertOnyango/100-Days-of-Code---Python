# Prime Number Checker Project
'''
An integer is considered prime if it's factors are only 1 and itself
i.e. it only has two factors (1 and itself) that when multiplied result in it
Division test: A prime number is divisible(with no remainders) only be one and itself
'''
# Function that checks if an integer is a prime number and returns TRUE if the number is prime
def is_prime(number):
    # Status that maintains the number is prime
    prime_status = True
    # 0 and 1 are prime numbers
    if number == 0 or number == 1:
        print("The numbers 0 and 1 are not prime numbers. A prime number needs to have two factors, one and itself. 1 only has one factor.")
        return True
    # Confirm a number greater than 1 is entered
    if number > 1:
        # Loop through integers from 2 to the number before our input, checking for factors
        for digit in range(2, number):
            # Divide each number and check for a zero remainder
            if (number % digit) == 0:
                print(f"Not a prime number. The number has a factor of: {digit}")
                prime_status = False
            else:
                prime_status = True

    # Set return values for function
    if prime_status:
        return True
    else:
        return False

test_number = int(input("Please input the number you want to test if it is a prime number: "))
print(is_prime(test_number))