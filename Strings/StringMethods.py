'''
Demonstrating the various string methods
'''

encoding_string = "My name is Ståle"
my_string = "This is the String Used for Demonstration"
#capitalize() - Converts only the first character to upper case
print(f"String after capitalizing {my_string.capitalize()}")
#count() - Returns the number of times a specified value occurs in a string
print(f"The count of 's' in \"{my_string}\" is {my_string.count('s')}")
#encode() - Returns an encoded version of the string
print(f"The encoded version of \"{my_string}\" is \"{encoding_string.encode()}\"")
#endswith() - Returns true if the string ends with the specified value
print(f"Does the string \"{my_string}\" end with 'on': \"{my_string.endswith('on')}\"")
#find() - Searches the string for a specified value and returns the position of where it was found
print(f"The string \"the\" is found at \"{my_string.find('the')}\" index position")
#lower() - Converts a string into lower case
print(f"The string \"{my_string}\" after converting to lower case is \"{my_string.lower()}\"")
#replace() - Returns a string where a specified value is replaced with a specified value
print(f"Replacing 's' with 't' in \"{my_string}\": \"{my_string.replace('s', 't')}\"")




