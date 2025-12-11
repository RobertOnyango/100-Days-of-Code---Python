# SYNTAX: [new_list for item in list if test]
# TODO 1: Write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared. Target Outptu: [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
'''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers =  [number*number for number in numbers]
print(squared_numbers)
'''

# TODO 2: Use list comprehension to filter out the even numbers from a series of numbers. 
'''
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# 1. Use list comprehension to convert the list_of_strings to a list of integers called numbers
numbers = [int(char) for char in list_of_strings]
# 2. Use list comprehension again to create a new list called result. This list should contain the even numbers from the list numbers
result = [number for number in numbers if number % 2 == 0]
print(result)
'''

# TODO 3: Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. You are going to create a list called result which contains the numbers that are common in both files. 
# e.g. if file1.txt contained:
# 1 
# 2 
# 3
# and file2.txt contained: 
# 2
# 3
# 4
# result = [2, 3]
'''
# Read each file to and extract the data as list
with open("file1.txt") as file:
    file1 = file.readlines()
# Strip the \n symbol and convert to int
file1_list = [int(char.strip("\n")) for char in file1]

# Read file 2 and convert to a list of int
with open("file2.txt") as file:
    file2 = file.readlines()
# Strip the \n symbol and convert to int
file2_list = [int(char.strip("\n")) for char in file2]

# Loop through each list and pick the common items
result = [number for number in file1_list if number in file2_list]

# answer = []
# # print(result)
# for number in file1_list:
#     if number in file2_list:
#         answer.append(number)

print(result)
'''

# TODO 4: Use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word. NOTE: To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
'''
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Split the sentence into a list of words
my_list = sentence.split()

result = {word:len(word) for word in my_list}
print(result)
'''

# TODO 5: Use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit. NOTE: To convert temp_c into temp_f use this formula: (temp_c * 9/5) + 32 = temp_f
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# {new_key:new_value for (key, value) in dictionary.items()}
weather_f = {day:(temperature_value * 9/5) + 32 for (day, temperature_value) in weather_c.items()}

print(weather_f)
