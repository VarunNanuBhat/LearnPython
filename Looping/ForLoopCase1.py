'''
Program to calculate sum of first "n" whole numbers
using for-loop and range function
'''

#Initializing sum variable to 0.
sum = 0
#Accept input from user
endPoint = int(input("Enter the end point: "))
#for-loop using range
for number in range(endPoint):
    sum = sum + number
print(f"The sum of first {endPoint} whole numbers is {sum}")

