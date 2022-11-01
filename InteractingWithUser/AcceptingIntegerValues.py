'''
Accept name, usn in string format and
marks of one subject from user in integer format
and check the type of value accepted using type.
'''

#Accepting inputs from user
name = input("Enter name of student: ")
usn = input("Enter USN of student: ")
marks = int(input("Enter marks: "))
#checking the type of entered details
print(type(name))
print(type(usn))
print(type(marks))



