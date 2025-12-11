student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(index)
    # print(row.student)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
# Read the csv data using the pandas library
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

print(data.to_dict()) # {'letter': {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}, 'code': {0: 'Alfa', 1: 'Bravo', 2: 'Charlie', 3: 'Delta', 4: 'Echo', 5: 'Foxtrot', 6: 'Golf', 7: 'Hotel', 8: 'India', 9: 'Juliet', 10: 'Kilo', 11: 'Lima', 12: 'Mike', 13: 'November', 14: 'Oscar', 15: 'Papa', 16: 'Quebec', 17: 'Romeo', 18: 'Sierra', 19: 'Tango', 20: 'Uniform', 21: 'Victor', 22: 'Whiskey', 23: 'X-ray', 24: 'Yankee', 25: 'Zulu'}}

# Create the new dictionary by reading each row in the dataframe, extracting the letter and code
# {new_key:new_value for (key,value) in dictionary.items()}
phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary) # {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

# Loop through each letter in the user input word
# NOTE" Manipulating dictinaries means that phonetic_dictionary[letter] gives the key i.e. the Letter
output_list = [phonetic_dictionary[letter] for letter in user_word]
print(output_list)
