'''
Accept name, usn and marks of one subject from user
and print the same using format method
in default order with more than one argument
'''

#Accepting inputs from user
name = input("Enter name of student: ")
usn = input("Enter USN of student: ")
marks = input("Enter marks: ")
#Displaying the entered details using format method
print("The name of student is: {}, USN is {} and marks is {}" .format(name, usn, marks))



