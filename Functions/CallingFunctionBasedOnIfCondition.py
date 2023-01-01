'''
Finding greatest of 2 numbers
using if condition
and calling the corresponding function.
'''

# defining 2 functions
def num1_is_greater(num1):
    print(f"{num1} is greater number")

def num2_is_greater(num2):
    print(f"{num2} is greater number")


# Accepting 2 numbers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# calling the corresponding function based on if condition.
if num1 > num2:
    num1_is_greater(num1)
else:
    num2_is_greater(num2)
