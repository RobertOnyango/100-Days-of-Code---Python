# Python code that uses the Pandas Library to create a CSV table summarizing the Primary_Fur_Color (Grey, Cinnamon, Black) from the Squirrel Census database 

import pandas

# Read the csv data
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251210.csv")

# Extract all the rows based on the colors: (Remember wach row is treated like a list, and the whole variable as a list of lists.)
# Gray squirrels
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
# Cinnamon
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
# Black
black_squirrels = data[data["Primary Fur Color"] == "Black"]

# Create the csv file
# 1. Create the dictionary
data_dict = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
}

# 2. Convert the dictionary to a dataframe
df = pandas.DataFrame(data_dict)

# 3. Create the csv file from the dataframce
df.to_csv("squirrel_summary.csv")



