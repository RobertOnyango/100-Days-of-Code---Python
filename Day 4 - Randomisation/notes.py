###### DAY 4: RANDOMIZATION AND PYTHON LISTS ######
#********** RANDOM MODULE **********#
#

# Python module with each module performing only one task as part of a whole
import random
# import my_module ######Module example

#Generate a random number N: a <= N <= b
random_integer = random.randint(1, 10)
print(random_integer)

# print(my_module.my_favourite_number) ######Module call example

# Generate random number x 0.0 <= x <= 1.0
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_1_to_10 = random.random() * 10
print(random_number_1_to_10)

# You can get 10 in this function call. Slightly different to above
random_float = random.uniform(1, 10)
print(random_float)

# Program to print random coin toss results
result = random.randint(0,1)
if result == 0:
    print("Heads!")
else:
    print("Tails!")

#*********** LIST ***********#
# List Data Structure allow us to group similar objects, which we can order

# List of fruits: Related data
fruits = ["apple", "mango", "pear"]

# Order in a list
print(fruits[0]) # apple
print(fruits[-1]) #pear: Last item in the list
print(fruits[-2]) #mango

# Edit an entry in the list
fruits[1] = "mangoes"
print(fruits) #['apple', 'mangoes', 'pear']

#Add a new entry at the end of the list
fruits.append("Watermelon")
print(fruits) #['apple', 'mangoes', 'pear', 'Watermelon']

fruits.extend(["pawpaw", "oranges"])
print(fruits) #['apple', 'mangoes', 'pear', 'Watermelon', 'pawpaw', 'oranges']

#https://docs.python.org/3/tutorial/datastructures.html


#********** INDEXERROR **********#
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[50]) # IndexError. No element at index 50

#Off by one
num_of_states = len(states_of_america) # 50
print(states_of_america[num_of_states - 1]) # Hawaii

# Nested Lists
fruits = ["Strawberries", "Rectarines", "Apples", "Grapes", "Peaches", "Cherries", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen) #[['Strawberries', 'Rectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Peaches'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]

print(dirty_dozen[1][1]) #Kale: List in index 1, Item in index 1 of selected list