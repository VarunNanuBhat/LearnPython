'''
Program to calculate average of
best 2 internal assessment marks of a student
from 3 internal assessments marks logical AND operator.
'''

#Accept 3 IA marks from user.
mark1 = int(input("Enter marks in 1st IA: "))
mark2 = int(input("Enter marks in 2nd IA: "))
mark3 = int(input("Enter marks in 3rd IA: "))
#The if block
if (mark1 < mark2) and (mark1 < mark3):
    avg = (mark2 + mark3)/2
elif (mark2 < mark3) and (mark2 < mark1):
    avg = (mark1 + mark3)/2
else:
    avg = (mark1 + mark2)/2
print("The average marks of a student is: {}" .format(avg))

