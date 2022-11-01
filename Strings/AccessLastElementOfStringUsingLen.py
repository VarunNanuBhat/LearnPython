'''
Access the very last element of a string
using len() function
'''

my_string = "Trying to access last element of the string"
#Find length of string
my_string_length = len(my_string)
#Accessing the last element
#Subtract 1 from string length because string index begins from 0.
indexing_character = my_string[my_string_length - 1]
print(f"The last element of {my_string} is {indexing_character}")

