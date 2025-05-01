#********** CLASS INHERITANCE **********
# Classes can inherit attributes and methods from each other
'''
class Fish(Animal):
    def __init__(self):
        super().__init__()

Animal = Name of the class we are inheriting from.
super().__init__() = Get everything (methods and attributes) from the Animal class. super = super class, initiliaze everything in the super class in our Fish class
'''

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        # Initializer recommeded but bot strictly required
        super().__init__()
    
    # We can also modify inherited methods
    def breathe(self):
        # Do Everything from the breathe() method in the super class
        super().breathe()
        # Modification
        print("Doing this under water.")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.breathe() # Inhale, exhale. Doing this under water.

#******* HOW TO SLICE LISTS & TUPLES **********#
# Note the slicing positions: 0 is at the beginning of the list(before the first elemet) and 7 is after the last element
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[2:5]) #["c", "d", "e"]
print(piano_keys[2:]) #["c", "d", "e", "f", "g"]
print(piano_keys[:5]) #["a", "b", "c", "d", "e"]
# The last digit give the slicing an increment of 2
print(piano_keys[2:5:2]) #["c", "e"]
print(piano_keys[::2]) #["a", "c", "e", "g"]
print(piano_keys[::-1]) #["g", "f", "e", "d", "c", "b", "a"]

print(piano_tuple[2:5]) #("mi", "fa", "so")

