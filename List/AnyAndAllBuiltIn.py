'''
"Any" and "All" built-ins.
"Any" - Returns "True" if any one element is true.
        Can be treated as an "OR" operation.
"All" - Returns "True" if all the elements are true.
        Can be treated as an "AND" operation.
'''

my_list_1 = [False, False, False]
my_list_2 = [False, True, False]
my_list_3 = [True, True, True]
# Performing operations on My_list_1.
print(f"Result for list 1 using \"any\": \"{any(my_list_1)}\"")
print(f"Result for list 1 using \"all\": \"{all(my_list_1)}\"")
# Performing operations on my_list_2.
print(f"Result for list 2 using \"any\": \"{any(my_list_2)}\"")
print(f"Result for list 2 using \"all\": \"{all(my_list_2)}\"")
# Performing operations on my_list_3.
print(f"Result for list 3 using \"any\": \"{any(my_list_3)}\"")
print(f"Result for list 3 using \"all\": \"{all(my_list_3)}\"")



