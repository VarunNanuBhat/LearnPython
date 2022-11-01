'''
Creating and modifying lists inside a tuple and tuple inside a list.
'''

#List inside a tuple
my_tuple = (1, [2.0, 'c'], "strings")
print(f"The combination of lists and tuples is \"{my_tuple}\"")
#Trying to Modify the list inside tuple
my_tuple[1][1] = 2
print(f"The tuple after modifying is \"{my_tuple}\"")

#Tuple inside a list
my_list = [1, (2.0, 'c'), "strings"]
print(f"The combination of tuples and lists is \"{my_list}\"")
#Trying to Modify the tuple inside inside
#User will get: TypeError: 'tuple' object does not support item assignment
my_list[1][1] = 2
print(f"The list after modifying is \"{my_list}\"")



