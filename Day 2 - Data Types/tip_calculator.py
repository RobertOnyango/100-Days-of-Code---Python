#Project that calculates the Tips of a group of friends at lunch
print("Welcome to the tip calculator!")
# Prompt the user for the total bill: Store bill as floating point
bill = float(input("What was the total bill? $"))

# Prompt the user for percentage of the bill to use as the tip
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

#Convert tip to percentage value(float)
actual_tip_percentage = tip / 100

#Total amount to pay as bill
total_amount = bill + (actual_tip_percentage * bill)

# Prompt the user for the number of people
people = int(input("How many people to split the bill? "))

# Split the total bill by the number of people
per_person_share = round(total_amount / people, 2)

print(f"Each person should pay USD {per_person_share}")

