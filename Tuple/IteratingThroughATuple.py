'''
Iterating through a tuple
using for-loop and printing
eah elements of a tuple
'''

my_tuple = ["coding", "with", "python", "is", "fun"]
#case 1: Using the index of the element in tuple
for element_index in range(len(my_tuple)):
    print(my_tuple[element_index])
else:
    print("Task completed")
#case2: Without using index of the element in tuple
for element in my_tuple:
    print(element)
else:
    print("Task completed")


