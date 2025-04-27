#********** CREATE NEW CLASS **********#

# REM: Naming a class should be in PascalCase
# class User:
#     # To leave a function or class empty, use the "pass" keyword
#     pass

# # Create a user object from the class
# user_1 = User()

# # Adding an attribute to the class (Variable associated with an object)
# user_1.id = "001"
# user_1.username = "robert"

# print(user_1.username)

#********** CONSTRUCTOR **********#
'''
The blueprint that allows us to specify what should happen when our object is being constructed (set variables, counters, switches etc as the starting values to the objects we'll create) i.e. INITIALIZING AN OBJECT.

Use the special function __init__: Inside this function is where we initialize.
''' 

class Car:
    '''
    Init function will be called everytime we create an object for the class.
    Self = Actual object being initializes.
    You can add as many parameters as you deem fit after the "self" argument. The added parameters will be received and used to set the objects attributes
    NOTE: When you add parameters the constructor (__init__ function), you're saying whenever a new object os being constructed from the class, it must provide the two arguments
    '''
    # Pass in seat argument
    def __init__(self, seats):
        #Once seat is received, it is used to set the Attribute for that object
        self.seats = seats

    # Initialize a method that changes the number of seats in the created object. 
    '''
    NOTE: A Method, unlike a function must have a self parameter as the first parameter. This means that when the function is called, it knows the method that called it.
    ''' 
    def enter_race_mode(self):
        self.seats = 2

#Calling the constructor i.e. pass in the seats argument as 5 so when the my_car obejcts is created, sekf.seats = 5.
my_car = Car(5)

# OPTION 2:
# 1. Create the my_car object first
my_car2 = Car(0)
# 2. Pass in the parameter for the Attribute
my_car2.seats = 7

# print(my_car.seats) #5
# print(my_car2.seats) #7

# my_car.enter_race_mode() # Amends the number of seats to 2 as per the funtion

# print(my_car.seats) #2

class User:
    
    def __init__(self, user_id, username):
        #Initialize attributes
        self.id = user_id
        self.username = username
        # You can initialize your arguments with a default value i.e. attribute that holds the count of your followers
        self.followers = 0
        # Attribute that holds the number of users you're following
        self.following = 0
    
    # Method that allows us to amend the number of followers in a created object i.e. Keeps track of the follow activity of our users
    def follow(self, user):
        # The user you're following, his/her followers count goes up by one
        user.followers += 1
        # Your following count goes up by one
        self.following += 1

# Construct object and pass in user_id Attribute at time of construction
user_1 = User("001", "robert")
# print(user_1.username) #robert

user_2 = User("002", "tabbs") 
# print(user_2.followers) #0

# User_1 decides to follow User_2
user_1.follow(user_2) 

#Print User_1 Followers
print(user_1.followers) #0

#Print User_1 Following
print(user_1.following) #1

#Print User_2 Followers
print(user_2.followers) #1

#Print User_2 Following
print(user_2.following) #0
