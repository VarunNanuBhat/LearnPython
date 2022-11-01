'''
Creating a list of tuples
by combining 3 tuples into 1
using zip()
'''

# Declaring tuples
name = ("Varun", "Hitesh", "Yashas")
usn = ("4ABC16CS103", "4ABC16CS025", "4ABC16CS108")
sem = ("3", "5", "7")
# zipping up 3 tuples to map values
student_details = zip(name, usn, sem)
# printing the elements inside student_details
for element in student_details:
    print(element)
else:
    print("Task completed")




