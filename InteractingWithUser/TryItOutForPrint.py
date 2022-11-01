'''
Accept name, usn in string format and
marks of one subject from user in integer format,
and print the same using format method
in default order with one argument
'''

#Accepting inputs from user
name = input("Enter name of student: ")
usn = input("Enter USN of student: ")
marks = int(input("Enter marks: "))
#Displaying the entered details using format method
print("The name of student is: {}" .format(name))
print()
print("The usn of student is: {}" .format(usn))
print()
print("The marks of student is: {}" .format(marks))

