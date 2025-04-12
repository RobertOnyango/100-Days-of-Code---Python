########## DAY 5: PYTHON LOOPS ##########
#********** FOR LOOPS **********#
fruits = ["Apple", "Peach", "Pear"]

# Give each item in the list a name i.e. Fruit
for fruit in fruits:
    # Print each fruit
    print(fruit) # Apple, Peach, Pear
    print(fruit + "pie") # Apple, Applepie, Peach, Peachpie, Pear, Pearpiey
#Take note of indentation: Print is not in For Loop
print(fruits) # ['Apple', 'Peach', 'Pear']

# Python program that generates a report for Student Exam scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# Sum()
# total_marks = sum(student_scores)
# print(total_marks)

# OR

# Variable to hold the total_score
total_scores = 0

for student_score in student_scores:
    total_scores += student_score

print(total_scores)

# Max()
# highest_mark = max(student_scores)
# print(highest_mark)

# OR

# Initialize variable to hold the highest mark
highest_mark = 0
for student_score in student_scores:
    # Check if current element is greater than highest_mark.
    if student_score > highest_mark:
        # If yes, assign its value as highest mark
        highest_mark = student_score

# Print the highest mark found
print(highest_mark)

#********** FOR LOOPS WITH RANGE() FUNCTION **********#
# Range() helps when you want to generate a range of numbers to loop through

# Prints number from 1-9
# for number in range(1, 10):
#     print(number) #1,2,3,4,5,6,7,8,9

# Prints the numbers 1-11, taking 3 steps
# for number in range(1, 11, 3):
#     print(number) # 1, 4, 7, 10

# A program that sums all the number from 1-100
# Variable to hold the sum
total = 0
# Loop through all the numbers from 1-100
for number in range(1, 101):
    # Add the number in range to total
    total += number
#Print sum
print(total)
