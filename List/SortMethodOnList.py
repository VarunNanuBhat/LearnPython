'''
Demonstrate sort method on python
'''

list_of_numbers = [2, 8, 6, 1, 9]
list_of_chars = ['b', 't', 'a', 's', 'l']
list_of_strings = ["Python", "Java", "Go", "Ruby"]
list_of_mixed_datatypes = [9, "Python", 'a', 1]
#sorting the lists in ascending order
list_of_numbers.sort()
print(f"Sorted list of numbers is \"{list_of_numbers}\"")
#sorting the lists in decending
list_of_chars.sort(reverse=True)
print(f"Sorted list of characters is \"{list_of_chars}\"")
#sorting the list "list_of_strings" using "sorted()" function.
sorted_list = sorted(list_of_strings)
print(f"The new list \"sorted_list\" is sorted:  \"{sorted_list}\"")
print(f"The original list, list of strings is unsorted: \"{list_of_strings}\"")
#User must get: TypeError: '<' not supported between instances of 'str' and 'int'
list_of_mixed_datatypes.sort()
print(f"Sorted list of mixed datatypes is \"{list_of_mixed_datatypes}\"")

