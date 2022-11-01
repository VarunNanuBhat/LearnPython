'''
Tuple concatenation and repetition
'''

my_tuple_1 = (1, 2.0, 'c', "strings")
my_tuple_2 = ("new", "tuple", "fun")
#concatenating tuple
conctenated_tuple = my_tuple_1 + my_tuple_2
print(f"The concatenated tuple is \"{conctenated_tuple}\"")
#tuple repetition
repeated_tuple = my_tuple_1 * 2
print(f"The tuple after applying repetition is \"{repeated_tuple}\"")

