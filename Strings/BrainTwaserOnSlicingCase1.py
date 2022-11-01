'''
Apply negative stepping and print string in reverse order
'''

my_string = "This is the string to be reversed"
#length of string
len_of_string = len(my_string)
reversed_string = slice(-1, -len_of_string - 1, -1)
print(f"The reversed string is \"{my_string[reversed_string]}\"")


