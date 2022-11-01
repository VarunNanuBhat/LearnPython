'''
ziping up tuples
of different lengths
'''

name = ("Varun", "Hitesh", "Yashas", "Gowrish")
sem = ("3", "5", "7")
# zipping up 2 tuples to map values
student_details = zip(name, sem)
# printing elements inside student_details
# The 4th element of "name" tuple will not be considered.
for element in student_details:
    print(element)
else:
    print("Task completed")

