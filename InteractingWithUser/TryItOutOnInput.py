'''
Accept name, usn in string format and
marks of one subject from user in integer format,
and print the same using format method
with more than one argument using positional formatting
'''

#Accepting inputs from user
name = input("Enter name of student: ")
usn = input()
marks = int(input("Enter marks: "))
#Displaying the entered details using format method
print("The name of student is: {0}, USN is {1} and marks is {2}" .format(name, usn, marks))



