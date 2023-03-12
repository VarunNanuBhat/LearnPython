'''
Program to print student details
and demonstrate class variable
'''

class StudentDetails:
    # Class variable
    college = "IIT"

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# Creating 2 objects for StudentDetails
obj1 = StudentDetails("Varun")
obj2 = StudentDetails("Hitesh")

# Printing the details along with class variable.
# The class variable can be accessed with class name and is common for all the objects of the class.
print(f"The student name is {obj1.get_name()} and college is {StudentDetails.college}")
print(f"The student name is {obj2.get_name()} and college is {StudentDetails.college}")
