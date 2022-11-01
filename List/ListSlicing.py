'''
List slicing using slice[:]
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#case 1: list[startPoint:endPoint]
list_with_SP_EP = my_list[0 : 5]
print(f"The first 5 elements of \"{my_list}\" are \"{list_with_SP_EP}\"")
#case 2: list[:endPoint]
list_with_EP = my_list[ :7]
print(f"The first 7 elements of \"{my_list}\" are \"{list_with_EP}\"")
#case 3: list[startPoint: ]
list_with_SP = my_list[5: ]
print(f"The elements in the list \"{my_list}\" after index value 5 are \"{list_with_SP}\"")
#case 4: list[startPoint:endPoint:step]
list_with_SP_EP_step = my_list[1 : 8 : 2]
print(f"The list in the range of index value 1 and 8 with step 2 is \"{list_with_SP_EP_step}\"")




