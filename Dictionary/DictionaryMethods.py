'''
Demonstrating the various dictionary methods
'''

my_dict = {
    "Name": "Varun",
    "Age": 23,
    "Phone Number": "9876543210"
}
# items() – Returns a list containing a tuple for each key value pair
print(f"List containing a tuple for each key value pair is {my_dict.items()}")
# keys() – Returns a list containing dictionary’s keys
print(f"List containing dictionary’s keys is {my_dict.keys()}")
# values() – Returns a list of all the values of dictionary
print(f"List of all the values of dictionary is {my_dict.values()}")
# update() – Updates dictionary with specified key-value pairs
my_dict.update({'Age': 24})
print(f"Dictionary after updating age is {my_dict}")
# pop() – Remove the element with specified key
my_dict.pop("Age")
print(f"Dictionary after popping \"Age\" is {my_dict}")
# get() – Returns the value of specified key
print(f"The phone number is {my_dict.get('Phone Number')}")
# copy() – Returns a copy of the dictionary
copied_dict = my_dict.copy()
print(f"The copied dictionary is {copied_dict}")
# clear() – Remove all the elements from the dictionary
copied_dict.clear()
print(f"The dictionaries is empty now: {copied_dict}")

