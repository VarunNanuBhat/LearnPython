'''
Find greatest of 2 numbers
using functions.
'''

def greatest_of_2_number(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater")
    else:
        print(f"{num2} is greater")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calling the function
greatest_of_2_number(num1, num2)