'''
Finding sum of 3 numbers
using functions having default arguments
'''

# creating the function
def sum_of_three_numbers(num1 = 10, num2 = 20, num3 = 30):
    # printing the values of each variable to understand what variable is assigned to what value
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")
    print(f"num3 = {num3}")
    sum = num1 + num2 + num3
    print(sum)


# different ways of calling the function
print("Sum of three numbers with default arguments")
sum_of_three_numbers()
print("Sum of three numbers with 2 arguments")
sum_of_three_numbers(5, 6)
print("Sum of three numbers with 3 arguments")
sum_of_three_numbers(5, 6, 7)
print("Sum of three numbers with positional arguments")
sum_of_three_numbers(num1=5, num2=6)
sum_of_three_numbers(num1=5, num3=7)
sum_of_three_numbers(num2=6, num3=7)
sum_of_three_numbers(num1=5, num2=6, num3=7)



