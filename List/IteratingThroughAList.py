'''
Iterating through a list
using for-loop and printing
eah elements of a list
'''

my_list = ["coding", "with", "python", "is", "fun"]
#case 1: Using the index of the element in list
for element_index in range(len(my_list)):
    print(my_list[element_index])
else:
    print("Task completed")
#case2: Without using index of the element in list
for element in my_list:
    print(element)
else:
    print("Task completed")


