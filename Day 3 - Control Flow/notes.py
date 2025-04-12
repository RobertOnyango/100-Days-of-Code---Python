#********** IF ELSE CONDITIONAL **********#
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: # Remember the colon :
    print("You can ride!") # IndentationError: Indentation marks begin of execution for the condition
else:
    print("Sorry you have to grow taller")

#Comparison operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

#NOTE: = is assigning, == conditional operator for comaparing

#********** MODULO OPERATOR (%)**********
# Returns the remainder

print(10 % 3) # 1

# Code that checks if the input user is even of odd
print("Welcome to the Odd or Even number checkup")
#Prompt user to add the number
number = int(input("Please input a number:")) #Remember to convert string to int

#Number is even is remainder divided by 2 is 0
if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

#********** IF ELIF CONDITIONS **********#
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age:"))
#     if age >= 13:
#         print("You can ride!")
#     else:
#         print("Wait a few more years.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age:"))
    if age <= 12:
        print("Please pay 100 bob")
    elif age <= 18:
        print("Please pay 150 bob")
    else:
        print("Please pay 250 bob")
else:
    print("Sorry you have to grow taller before you can ride.")

#********** MULTIPLE IFs **********#
# All the conditions are checked unlike in elif where only one condition will tested
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# Variable to hold total bill
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Child tickets are {bill}.")
    elif age <= 18:
        bill = 7
        print(f"Teens tickets are {bill}.")
    else:
        bill = 12
        print(f"Adult tickets are {bill}.")
    #Ask user if they'd like an additional photo
    wants_photo = input("Do you want a photo taken? Take y for Yes and n for No.")
    if wants_photo == "y":
        #Add $3 to total bill + 3 = bill
        bill += 3
        print(f"Your total bill is: {bill}")
    else:
        print(f"Your total bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

#********** LOGICAL OPERATORS **********/
# and
# or
# not
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age <= 55: #45 <= age <=55
        print ("Free ride on us")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

