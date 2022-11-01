'''
Program to print "n" natural numbers
within a given range and
stop the execution of program
if the number is divisible by 10
using break statement
'''

#Accept input from user
startPoint = int(input("Enter the start point: "))
endPoint = int(input("Enter the end point: "))
#while loop
while startPoint < endPoint:
    startPoint = startPoint + 1
    if startPoint % 10 == 0:
        break
    else:
        print(startPoint)


