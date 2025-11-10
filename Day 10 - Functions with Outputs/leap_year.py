# A function that indicates whether the year is a Leap Year
def is_leap_year(year):
    # Check if year is divisible by 4, if there's no remainder => Leap AND check if it is divisible by 100, if there's a remainder => Leap. 
    # The condition above checks if the number is both fully divisible by 4 and not fully divisible by 100
    # Check if it is divisible by 400, no remainder = Leap
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(1974))
