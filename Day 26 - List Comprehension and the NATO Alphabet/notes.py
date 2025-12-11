# HOW TO CREATE LISTS USING LIST COMPREHENSION

'''
# How would you increase each number in a list of integers by one?
numbers = [1, 2, 3]
new_numbers = []

for num in numbers:
    add_1 = num + 1
    new_numbers.append(add_1)

print(new_numbers)
'''

# Alternatively, create a LIST COMPREHENSION
# Syntax: new_list = [new_list for item in list]
'''
numbers = [1, 2, 3]
new_list = [num + 1 for num in numbers]
print(new_list)
'''

# Predict what new_list will contain in the case below: It goes into the string, loops through each letter as it adds it as an individual character in the new_list
'''
name = "Angela"
new_list = [letter for letter in name]
print(new_list) # ['A', 'n', 'g', 'e', 'l', 'a']
'''

# CHALLENGE: Take a range (1,5), and create a list where each number in the list is doubled
'''
range_list = [num*2 for num in range(1,5)]
print(range_list)
'''

# CONDITIONAL LIST COMPREHENSION: Adding two keywords = if and test
# Syntax: new_list = [new_list for item in list if test] => Only perfom the action if the test passes
'''
# Example 1:
original_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# New list with only the names with less than 5 characters
short_names = [name for name in original_names if len(name) < 5]
print(short_names)
# Challenge: Take from teh list the names with 5 letters or more and turn these names to all CAPS
all_caps = [name.upper() for name in original_names if len(name) > 4]
print(all_caps)
'''

# HOW TO USE DICTIONARY COMPREHENSION

#SYNTAX - Create a new dictionary from items in a list: new_dict = {new_key:new_value for item in list}

# SYNTAX - Create a new dictionary from the values in an existing dictionary: new_dict = {new_key:new_value for (key,value) in dict.items()}

'''
import random

original_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Generate random scores for each of the names in the list
student_scores = {student:random.randint(1, 100) for student in original_names}

print(student_scores)

# Using the new dictionary student_scores, create a new dictionary called passed_scores where the student_score values > 60
# {new_key:new_value for (key,value) in dictionary.items()}
passed_scores = {student:scores for (student,scores) in student_scores.items() if scores >= 60}
print(passed_scores)
'''

# HOW TO ITERATE OVER PANDAS DATAFRAME

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionary
for key in student_dict:
    print(key) # student, score
    print(student_dict[key]) #['Angela', 'James', 'Lily'], [56, 76, 98]

# NOTE: You can loop thrugh a pandas dataframe quite similarly as you would a normal dictionary
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for key in student_data_frame.items():
    print(student_data_frame.score)

# Loop through each of the r ows of the data_frame instead of the columns
for (index, row) in student_data_frame.iterrows(): 
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if (row.student) == "Angela":
        print(row.score)
