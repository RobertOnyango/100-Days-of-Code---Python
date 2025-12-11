# READING CSV DATA IN PYTHON

'''
# Open the weather_data csv file open()
with open("weather_data.csv") as data_file:
    # Add each row of data to a list called data
    data = data_file.readlines()

print(data)
'''

'''
# Access the csv data using the csv library to read the csv data from the file
import csv

with open("weather_data.csv") as data_file:
    # Create the csv.reader object
    data =  csv.reader(data_file)
    # print(data) => <_csv.reader object at 0x000001E234D6EBC0>
    
    # Loop through this object to get each record as a row
    for row in data:
        print(row) # => ['day', 'temp', 'condition'] ['Monday', '12', 'Sunny'] ['Tuesday', '14', 'Rain']
                      
    # List variable that will hold all the temperature values
    temperatures = []
    for row in data:
        # Exclude the 1st item in the list, the word 'temp'
        if row[1] != "temp":
            # Append the values, converted to an integer from string
            temperatures.append(int(row[1])) 
    print(temperatures)
'''

# PANDAS Library - Data Analysis Library for tabular data
# https://pandas.pydata.org/docs/
import pandas

# Read the csv file using the Pandas Library
data = pandas.read_csv("weather_data.csv")
# print(data) - reads all the data. Data type = <class 'pandas.core.frame.DataFrame'>
# print(data["temp"]) # Pandas automatically identifies the temp column and prints the column value in a series of lists. Data Type = <class 'pandas.core.series.Series'>
# NOTE: The whole table in pandas i.e. data is like a dataframe and a single column is a series(like a list) i.e. data["temp"]

# Convert the data to a dictionary
data_dict = data.to_dict()
print(data_dict) # Prints out dictionaries as columns e.g. {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# Convert the series to a list
temp_list = data["temp"].to_list()
print(temp_list) # [12, 14, 15, 14, 21, 22, 24]

# Find the average temperature
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

# Find the average using the mean function in the pandas library
print(f" The mean is: {data["temp"].mean()}")

# What is the maximum temperature value
print(f"The maximum temperature value is: {data["temp"].max()}")

# Get the all the condition data from the condition column
print(data["condition"]) # Treaing the Dataframe like a 'dictionary' where we are pulling the data using a key i.e. data["condtion"]
print(data.condition) # Treating the DataFrame like an 'object' from a class where we pulling data as an attribute i.e. data.condition

# Get the data in Row
# SYNTAX: Get a hold of the data table i.e. data[], then inside the data table, get the day column i.e. data.day
print(data[data.day == "Monday"]) # 0  Monday    12     Sunny

# Which row of data had the maximum day of the week?
print(data[data.temp == data.temp.max()])

# NOTE: If we take our day table and we only put the name of the columns inside the square brackets i.e. data[data.condition], we would get the entire column
# NOTE: If we put a condition inside the square brackets such that the column name matches a certain condtion i.e. data[data.condition == "Sunny"], we get the specific rows where this condition matches

# What if we want to extract the weather condition of the day Monday?
# Extract the entire row of Monday
monday = data[data.day == "Monday"]
# From the row extract the condition
print(monday.condition)

# Convert Monday's temperature to  Farenheit
# Extract Monday's temperature HINT: Use [] to get a single value from the series(list)
monday_temp = monday.temp[0]
print(monday_temp * 9/5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
# Convert the dictionary to a DataFrame
data_students = pandas.DataFrame(data_dict)
print(data_students)
# Convert the data frame to a newly created csv file
data_students.to_csv("new_data.csv")
