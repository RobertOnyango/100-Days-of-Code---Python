#********** PYTHON DICTIONARY **********#
# Dictionaries: Allow us to group together and tag related pieces of information
# Key-Value Pair. {Key: Value} {Key1: Value1, Key2: Value2}
# You can add a comma to the last element in your dictionary

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    123: "This is a test for int key",
}

# Print element1 with Key = Bug. Be careful to use the correct keys and data types for the keys.
print(programming_dictionary["Bug"]) # An error in a program that prevents the program from running as expected.

print(programming_dictionary[123]) # This is a test for int key

# Adding data to the dictionary: dictionary[Key]: Value
programming_dictionary["Loop"] = "Doing something over and over again."
print(programming_dictionary)

# Edit an item in the dictionary
programming_dictionary["Bug"] = "This is a new bug input"
print(programming_dictionary["Bug"]) # This is a new bug input

# Looping through a dictionary
for key in programming_dictionary:
    print(key) # Prints the Key
    print(programming_dictionary[key]) # Prints the value for each key

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary) # Empty dictionary

#********** NESTED LISTS AND DICTIONARIES **********#
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in  a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
#Print out Lille
print(travel_log["France"][1])

# NESTED LIST
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1]) # D

#NESTED DICTIONARY
travel_log2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

print(travel_log2["France"]["cities_visited"][2])#Dijon

