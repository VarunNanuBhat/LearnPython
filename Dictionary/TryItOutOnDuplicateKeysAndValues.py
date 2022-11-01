'''
Dictionaries do not support
duplicate keys but
support duplicate values
'''

# Case 1: Trying to add duplicate keys
my_dict = {
    "Name": "Varun",
    "Age": 23,
    "Phone Number": "9876543210",
    "Phone Number": "0123456789"
}
print(f"Only the second phone number will be printed {my_dict}")
# Case 2: Trying to add duplicate values
my_dict = {
    "Name": "Varun",
    "Age": 23,
    "Phone Number 1": "9876543210",
    "Phone Number 2": "9876543210"
}
print(f"Both the phone number will be printed {my_dict}")


