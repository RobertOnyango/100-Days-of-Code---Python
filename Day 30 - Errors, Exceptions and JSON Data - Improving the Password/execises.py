# Challenge 1: The code as is will crash and give an IndexError.

# Objective: Use what you've learnt about exception handling to prevent the program from crashing. If the user enters something that is out of range just print a default output of "Fruit pie".

# IMPORTANT: The exception handling should NOT allow each fruit to be printed when there is an exception. e.g. it should not print out Apple pie, Pear pie and Orange pie, when there is an exception it should only print "Fruit pie". 

'''
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

make_pie(4)
'''

'''
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + "pie")

make_pie(100)
'''

# Challenge 2: The code will crash and give you a KeyError because some of the posts in the facebook_posts don't have any "Likes". 
# Objective: Use what you've learnt about exception handling to prevent the program from crashing. 

'''
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        total_likes = total_likes + post['Likes']
    
    return total_likes
'''

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try: 
            total_likes = total_likes + post['Likes']
        except KeyError:
            # If there is a Keyword error, pass the post in the loop
            pass

    return total_likes 

print(count_likes(facebook_posts))