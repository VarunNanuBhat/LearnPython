'''
Modifying a tuple by
converting it into list
'''

my_tuple = (1, 2.0, 'c', "strings")
print(f"The tuple before modification is \"{my_tuple}\"")
#converting tuple to list
my_list = list(my_tuple)
#Modifying the list
my_list[3] = 5
#converting list back to tuple
my_tuple = tuple(my_list)
print(f"The tuple after modification is \"{my_tuple}\"")



