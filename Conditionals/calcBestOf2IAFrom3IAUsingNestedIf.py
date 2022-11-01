'''
Program to Program to calculate
average of best 2 internal assessment marks of a student
from 3 internal assessments marks using nested if.
'''

#Accept 3 IA marks from user.
mark1 = int(input("Enter marks in 1st IA: "))
mark2 = int(input("Enter marks in 2nd IA: "))
mark3 = int(input("Enter marks in 3rd IA: "))
#The first if-block (Finding the smallest no)
#check if mark1 is lesser then mark2
if mark1 < mark2:
    #if inside if (nested if)
    #check if mark1 is lesser than mark3
    if mark1 < mark3:
        #calculate average of best 2 IA.
        avg = (mark2 + mark3)/2
    else:
        avg = (mark1 + mark2)/2
elif mark2 < mark3:
    avg = (mark1 + mark3)/2
else:
    avg = (mark1 + mark2)/2

print("The average marks of a student is: {}" .format(avg))


