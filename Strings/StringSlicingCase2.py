'''
String slicing using slice[:]
'''

my_string = "This is the string used for slicing"
#case 1: string[startPoint:endPoint]
string_with_SP_EP = my_string[0 : 10]
print(f"The first 10 characters of \"{my_string}\" are \"{string_with_SP_EP}\"")
#case 2: string[:endPoint]
string_with_EP = my_string[ :15]
print(f"The first 15 characters of \"{my_string}\" are \"{string_with_EP}\"")
#case 3; string[startPoint: ]
string_with_SP = my_string[15: ]
print(f"The chacters in the string \"{my_string}\" after index value 15 are \"{string_with_SP}\"")
#case 4: string[startPoint:endPoint:step]
string_with_SP_EP_step = my_string[1 : 10 : 2]
print(f"The string in the range of index value 1 and 10 with step 2 is \"{string_with_SP_EP_step}\"")





