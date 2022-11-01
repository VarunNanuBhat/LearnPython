'''
Using membership operator
in a dictionary to check
if a key is present
in a dictionary or not.
'''

my_dict = {
    "Name": "Varun",
    "Age": 23,
    "Phone Number": "9876543210"
}

if "Name" in my_dict:
    print("Key \"Name\" is present in dictionary")

if "Blood group" not in my_dict:
    print("Key \"Blood group\" is not present in dictionary")

