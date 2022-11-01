'''
Program to access a character in a string
whose index is greater then the length of string.
'''

my_string = "Trying to access string index which does not exist"
#Find length of string
my_string_length = len(my_string)
#Indexing arbitary value greater than my_string_length
indexing_value = my_string_length + 5
indexing_character = my_string[indexing_value]
print(f"The string element at {indexing_value} is {indexing_character}")

