'''
python program to accept name and marks of 2 students
and print the result in the format shown below.
Name    |  Marks
Varun   |  25
Hitesh  |  30

String alignment can also be provided with the help of following operators:
	“<”   : Left alignment
	“>”   : Right alignment
	“^”   : Center alignment
'''

# Accepting input from user
student_1_name = input("Enter name of student 1: ")
student_1_marks = int(input("Enter marks of student 1: "))
student_2_name = input("Enter name of student 2: ")
student_2_marks = int(input("Enter marks of student 2: "))
# Using format method to print the result in desired format.
print("{0:8} | {1:8}".format("Name", "Marks"))
print("{0:8} | {1:<8}".format(student_1_name, student_1_marks))
print("{0:8} | {1:<8}".format(student_2_name, student_2_marks))


