#********** DATA TYPES **********#

#String
len("Hello")

#Subscripting: Pull single character from string
print("Hello"[1]) #e

#Get the last character from the string
print("Hello"[-1]) #o

#String
print("123" + "456") #123456

#Integers
print(123 + 456) #579

#Large Integers: _ replace commas for our reading
print(123_456_789) #123,456,789

#Float
print(3.142)

#Boolean: True or False

age = 12
print("You are" + str(age) + "years old")

#********** TYPE ERROR, CHECKING and CONVERSION **********#

# Each function in Python requires a specific data type as input other you get a Type Error
#len(12345) Type Error: Len() doesn't accept type int as input
len("12345")

#Type Checking
print(type("Hello")) #Type() tell us the data type: <class 'str'>
print(type(1234)) #<class 'int'>
print(type(True)) #<class 'bool'>
print(type(34.988)) #<class 'float'>

#Type conversion / Type Casting
int("123") #int() convert the string "123" to an integer
print(int("123") + int("456")) #579
#ValueError: You can't convert some input e.g. int("abc") will bring an error

#You can also convert using the following functions:
# int()
# float()
# str()
# bool()

user_name = input("Enter your name") #<class 'str'>
length_of_name = len(user_name) #<class 'int'>

print("Number of letters in your name: " + str(length_of_name))

#OR
print("Number of letters in your name is: " + str(len(input("What is your name?"))))

#********** MATHEMATICAL OPERATIONS **********#
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3) #Result is always a Float: (Implicit Type casting)
print(6 // 3) #Result is always an Integer: Different type of division operator that removes the decimal places from the result
print(5 // 3) #Answer is 1.
print(2 ** 3) #2 to the power of 3

#Priority: BODMAS rule
print(3 * 3 + 3 / 3 - 3) #Ans: 7.0

print(3 * (3 + 3) / 3 - 3) #Ans: 3.0

#********** NUMBER MANIPULATION **********#
bmi = 84 / 1.65 ** 2
print(bmi) #30.85399449035813

# Flooring a number
print(int(bmi)) #30

# Rounding a number up or down
print(round(bmi)) #31

# Round the number to the number of decimal places you'd like
print(round(bmi, 3)) #30.854

#Assignment Operators (+=, -=, *=, /=)
score = 0
#User scores a point
score += 1
print(score) #1

#F-stings (Makes it possible to mix different data types e.g. integers and strings
score = 109
height = 1.0 #float
is_winning = True #boolean
print(f"Your score is {score}, your height is {height}, and your are {is_winning}")
