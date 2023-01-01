'''
Find greatest of 2 numbers
using functions and return the result
using return keyword.
Return keyword is used to break the execution of program.
'''

def greatest_of_2_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calling the function and assigning the result to a variable
greater_num = greatest_of_2_number(num1, num2)
print(greater_num)