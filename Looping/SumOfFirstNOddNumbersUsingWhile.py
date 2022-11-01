'''
Program to find sum of first "n" odd
using while loop
'''

#Initialising variables
number = 0
sum = 0
#Accept input from user
endPoint = int(input("Enter the end point: "))
#while loop
while number <= endPoint:
    if number % 2 != 0:
        sum = sum + number
    number = number + 1
print(f"The sum of first {endPoint} numbers is {sum}")

