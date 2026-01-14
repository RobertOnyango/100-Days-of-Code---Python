# Question 1:
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham) # 1 2 'yes please!' 0
 
bar(1, 2) 

# Question 2: 
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham) # 4 2 'nah' 0
 
bar(toast='nah', spam=4, eggs=2) 

# Question 3:
def test(*args):
    print(args) # Tuple
 
test(1,2,3,5) 

# Question 4: 
def test(*args):
    print(args) #(1,2,3,5)
 
test(1,2,3,5)

# Question 5: 
def all_aboard(a, *args, **kw): 
    print(a, args, kw) #4 (7, 3, 0) {'x': 10, 'y': 64}
 
all_aboard(4, 7, 3, 0, x=10, y=64)