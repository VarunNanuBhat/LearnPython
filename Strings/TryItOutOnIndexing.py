'''
Program to access individual elements
of a string using floating index value.
Note: The code snippet will give an error because we can access string indexes using floating point numbers'''

#Declaring a string
my_string = "Trying to access string character using floating point index"
#Accessing element at first position
element_at_first_pos = my_string[0]
#Accessing element at second position
element_at_second_pos = my_string[1.0]
#Accessing element at tenth position
element_at_tenth_pos = my_string[10]

print(f"Element at first position is {element_at_first_pos}")
print(f"Element at second position is {element_at_second_pos}")
print(f"Element at tenth position is {element_at_tenth_pos}")

