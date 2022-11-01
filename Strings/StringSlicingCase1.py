'''
String slicing using slice() function
'''

my_string = "This is the string used for slicing"
#case 1: slice(startPoint)
string_with_EP = slice(6)
print(f"The first 6 characters of \"{my_string}\" are \"{my_string[string_with_EP]}\"")
#case 2: slice(startPoint, endPoint)
string_with_SP_EP = slice(5, 15)
print(f"The string in the range of index value 5 and 15 is \"{my_string[string_with_SP_EP]}\"")
#case 3: slice(startPoint, endPoint, step)
string_with_EP_SP_step = slice(5, 15, 2)
print(f"The string in the range of index value 5, 15 with a step of 2 is \"{my_string[string_with_EP_SP_step]}\"")


