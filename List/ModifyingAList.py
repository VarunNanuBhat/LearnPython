'''
Modifing a list at any given position
'''

my_list = [1, 2.0, 'c', "strings"]
print(f"The list before modification is \"{my_list}\"")
#Accepting the element and list index to be modified
new_element = input("Enter the new element: ")
index_value_changed = int(input("Enter the index of list to be modified: "))
#Modifying the list
my_list[index_value_changed] = new_element
#printing the new list
print(f"The list after modification is \"{my_list}\"")



