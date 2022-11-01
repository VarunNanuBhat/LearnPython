'''
Iterating through a string
using for-loop and printing
the characters of the string
'''

my_string = "This is the string we will be using"
#case 1: Using the index of the character in string
for char_index in range(len(my_string)):
    print(my_string[char_index])
else:
    print("Task completed")
#case2: Without using index of the character in string
for char in my_string:
    print(char)
else:
    print("Task completed")

