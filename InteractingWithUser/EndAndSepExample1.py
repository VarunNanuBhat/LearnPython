'''
Accept name, usn in string format and
marks of one subject from user in integer format,
and print name and usn in one line using end parameter
and USN and marks in usn:marks format using sep parameter
'''

#Accepting inputs from user
name = input("Enter name of student: ")
usn = input("Enter USN of student: ")
marks = int(input("Enter marks: "))
#Displaying the entered details
print("The name of student is: ", name, end = " ")
print("and the usn of student is: ", usn)
print(usn, marks, sep = ":")



