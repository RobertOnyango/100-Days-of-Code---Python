# #************ PIZZA ORDERING PROGRAM **********#
# print("Welcome to Python Pizza Deliveries!")
# bill = 0
# # Prompt user for pizza size store in variable 'size'
# size = input("What size pizza do you want? S, M or L: ")
# # Calculate they much they need to pay based on size
# if size == "S":
#     bill += 15
#     print (f"Price of small pizza is: {bill}")
# elif size == "M":
#     bill += 20
#     print(f"Price of medium pizza is: {bill}")
# elif size == "L":
#     bill += 25
#     print(f"Price of large pizza is: {bill}")
# else:
#     print(" Incorrect entry. Please enter S, M or L.")
#
# # Calculate how much new bill will be with additional pepperoni
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#         print(f"Your new bill is: {bill}")
#     else:
#         bill +=3
#         print(f"Your new bill is: {bill}")
# else:
#     print("Please enter the correct input.")
#
# # Calculate new bill based on extra cheese yes or no selection
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# if extra_cheese == "Y":
#     bill += 1
#     print(f"Your final bill is {bill}")
# else:
#     print(f"Your final bill is {bill}")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size.")

# todo: work out how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
