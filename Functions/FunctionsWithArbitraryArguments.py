'''
Creating and calling functions with
arbitrary number of arguments using *args.
*args treats positional parameters as tuples of parameters.
'''

def sum_of_n_numbers(*args):
    print(args)               # just to check how args looks like.
    return sum(args)


result_of_2_parms = sum_of_n_numbers(10, 20)
print(result_of_2_parms)
result_of_3_parms = sum_of_n_numbers(10, 20, 30)
print(result_of_3_parms)
result_of_4_parms = sum_of_n_numbers(10, 20, 30, 40)
print(result_of_4_parms)