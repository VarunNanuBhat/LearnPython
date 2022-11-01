'''
Demonstrating the various list methods
'''

my_list = [1, 2.0, 'c', "strings"]
another_list = ["Python", "is", "fun"]
#append() - Adds an element at the end of the list.
my_list.append("last element")
print(f"The list after appending is \"{my_list}\" ")
#copy() - Returns a copy of the list.
copied_list = my_list.copy()
print(f"The copied version of list is \"{copied_list}\"")
#count() - Returns the count of the specified element.
count_of_a = my_list.count('c')
print(f"The count of \"c\" in list is \"{count_of_a}\"")
#extend() - Adds all the elements of a list to the end of another list.
print(f"The combination of 2 lists is \"{my_list.extend(another_list)}\"")
#insert() - Adds an element at the specified position of a list.
my_list.insert(2, 'a')
print(f"Adding \"a\" at 3rd position of a list: \"{my_list}\"")
#pop() - Removes an element at the specified position.
my_list.pop(3)
print(f"List after popping element at index \"3\" is \"{my_list}\"")




