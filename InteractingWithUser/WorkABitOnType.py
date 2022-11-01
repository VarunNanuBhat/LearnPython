'''
Accept name, USN and marks of one subject from user
and check the type of value accepted using type.
'''

#Accepting inputs from user
name = input("Enter name of student: ")
usn = input("Enter USN of student: ")
marks = input("Enter marks: ")
#checking the type of entered details
print(type(name))
print(type(usn))
print(type(marks))