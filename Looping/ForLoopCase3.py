'''
Program to calculate sum of "n" odd numbers
between a given range using
for-loop and range function
'''

#Initializing sum variable to 0.
sum = 0
#Accept input from user
startPoint = int(input("Enter the start point: "))
endPoint = int(input("Enter the end point: "))
#for-loop using range
for number in range(startPoint, endPoint + 1, 2):
    sum = sum + number
print(f"The sum of odd numbers between {startPoint} and {endPoint} is {sum}")

