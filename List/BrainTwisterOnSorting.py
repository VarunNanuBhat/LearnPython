'''
sorting a list containing strings
with different cases and
perform case-insensitive.
'''


my_list = ["coding", "with", "Python", "is", "fun"]
my_list.sort(key = str.lower)
print(f"The sorted list is \"{my_list}\"")



