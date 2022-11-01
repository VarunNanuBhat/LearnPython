'''
Demonstrating the various list functions
'''

my_list = [1, 2, 3, 4, 5]
my_string = "Python is fun"
#max() - Returns the maximum element in the list.
print(f"The maximum number in \"{my_list}\" is \"{max(my_list)}\"")
#min() - Returns the minimum element in the list.
print(f"The minimum number in \"{my_list}\" is \"{min(my_list)}\"")
#list() - Returns a list.
print(f"String \"{my_string}\" converted to list is \"{list(my_string)}\"")
#del() - Deletes the list.
del(my_list)
#User must get: NameError: name 'my_list' is not defined
print(f"Deleting the list \"{my_list}\"")



