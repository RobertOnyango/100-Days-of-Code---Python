# A program that converts students scores stored in a dictionary to grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# New dictionary to hold the student grades
student_grades = {}

# Loop through each key to get the values and work with them
for key in student_scores:
    # Convert each key to grade
    if student_scores[key] > 90:
        # Store the key and value in new dictionary
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)