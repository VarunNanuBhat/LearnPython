'''
Accept two numbers in integer format
and print it back to user using fstrings
after swapping the 2 numbers
'''

#Accepting inputs from user
num1 = int(input("Enter value for number 1: "))
num2 = int(input("Enter value for number 2: "))
#Swap to numbers
num1, num2 = num2, num1
print(f"The numbers after swapping are {num1} and {num2}")

