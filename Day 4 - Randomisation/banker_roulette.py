#********** BANKER ROULETEE **********#
# Code that picks a name from the list randomly
import random

# Friends list has 5 elements, index is 0 -4
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# #Pick a random number between 0 and 4
# random_list_index = random.randint(0,4)
#
# #Print name where random index is selected
# print(friends[random_list_index])

# OPTION 2: Use random.choice() to get random item from list
print(random.choice(friends))