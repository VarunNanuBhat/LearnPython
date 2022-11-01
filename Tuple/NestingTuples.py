'''
Nesting tuples and
accessing elements
of a nested tuples
'''

#Creating a nested tuple
my_nested_tuple = (5.0, (1, 'a', "Hi",), 10)
#Accessing element at second position
element_at_second_pos = my_nested_tuple[1]
print(f"The element at second position is \"{element_at_second_pos}\"")
#Accessing element at first position of a nested tuple i.e., 1
element_1 = my_nested_tuple[1][0]
print(f"The element at first position of a nested tuple is \"{element_1}\"")



