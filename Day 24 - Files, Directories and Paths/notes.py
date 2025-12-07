'''
# Open the file in Python
file = open("my_file.txt")
# Read the contents of the file
contents = file.read()
print(contents)
# Close the file to free up compute resources
file.close()
'''

# Alternative to automatically close a file without explicitly using the close() -> use the keywords with ... as
'''
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
'''

# Write to a file - Change open mode to write "w" which formats the file and updates your new text or append "a" which updates your text as new lines without formatting the initial file. The default is read "r" which is read only.
'''
with open("my_file.txt", mode="a") as file:
    file.write("\nThis is new text.")
'''

# When you open a file that doesn't exist, the new file will be created
'''
with open("new_file.txt", mode="w") as file:
    file.write("New text")
'''

# UNDERSTAND RELATIVE AND ABSOLUTE FILE PATHS
# Absolute File Paths start from the root of the File system i.e. / in Linux, C:/ in Windows.
# Relative File Paths: Depends on where you currently are in the file system. Here we use '../../' for example to move upwards by two steps in the file system

# Use absolute path
'''
with open("/Users/Hp/Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)
'''

# Use relative path to notes: Go back Five steps to HP folder
with open("../../../../../Desktop/my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)

