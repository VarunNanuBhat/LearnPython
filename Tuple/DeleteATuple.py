'''
Delete a tuple
'''

my_tuple = (1, 2, 3, 4, 5)
print(f"The tuple declared is \"{my_tuple}\"")
#Deleting a tuple
del my_tuple
#NameError: name 'my_tuple' is not defined
print(f"after deleting a tuple we cannot access it: \"{my_tuple}\"")

