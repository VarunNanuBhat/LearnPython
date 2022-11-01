'''
Printing integer values with string.
'''

age = 23
# Try to print the below statement
# User will get: TypeError: can only concatenate str (not "int") to str
print("I am " + age + " years old")
# Change the type to str
print("I am " + str(age) + " years old")


