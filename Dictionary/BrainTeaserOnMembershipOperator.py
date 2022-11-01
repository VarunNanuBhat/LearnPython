'''
Using membership operator
in a dictionary to check
if a value is present
in a dictionary or not.
'''

my_dict = {
    "Name": "Varun",
    "Age": 23,
    "Phone Number": "9876543210"
}

if "Varun" in my_dict:
    # The if block won't be executed
    print("Value \"Varun\" is present in dictionary")

if "Varun" not in my_dict:
    # The else block will be executed because of "not in"
    # but would not yield proper results
    print("Value \"Varun\" is not present in dictionary")

