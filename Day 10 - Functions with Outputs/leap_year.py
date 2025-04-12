# A function that indicates whether the year is a Leap Year
def is_leap_year(year):
    # Check if year is divisible by 4, no remainder = Leap AND
    # Check if it is divisible by 100, remainder = Leap
    # Check if it is divisible by 400, no remainder = Leap
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(1974))
