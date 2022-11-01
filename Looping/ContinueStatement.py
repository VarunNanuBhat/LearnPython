'''
Program to print first "n" natural numbers
which are not divisible by 5 using continue statement
'''

#Intializing variables
number = 0
#Accept input from user
endPoint = int(input("Enter the end point: "))
#while loop
while number < endPoint:
    number = number + 1
    if number % 5 == 0:
        continue
    else:
        print(number)





