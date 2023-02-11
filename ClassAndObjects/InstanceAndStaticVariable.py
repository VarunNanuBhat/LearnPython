'''
Defining a class and assigning variables
using init method and also to
demonstrate instance and static variables.
'''

# Defining a class to print user details
class PrintUserDetails:
    # Creating static variables
    college_name = "PESITM"

    # The __init__ method to assign name and usn for an object.
    # init method is used to assign values for instance variables.
    def __init__(self, name, usn):
        print("This method is invoked automatically when the object is created")
        self.name = name
        self.usn = usn

    def print_user_details(self):
        print(f"The name is {self.name}")
        print(f"The USN is {self.usn}")
        print(f"The college name is {self.college_name}")

# Creating objects for PrintUserDetails class
# Here we are actually passing 3 arguments. The first arg is the object itself which is assigned to self.
obj1 = PrintUserDetails("Varun",  "CS103")
obj2 = PrintUserDetails("Hitesh", "CS065")

# Calling the objects to print details by passing name and usn.
obj1.print_user_details()
obj2.print_user_details()

# You can also access and print static variables of a class by referring the class name
print(PrintUserDetails.college_name)
