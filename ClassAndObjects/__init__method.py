'''
Defining a class
and assigning variables
using init method.
'''


# Defining a class to print user details
class PrintUserDetails:
    # The __init__ method to assign name and usn for an object

    def __init__(self, name, usn):
        print("This method is invoked automatically when the object is created")
        self.name = name
        self.usn = usn

    def print_user_details(self):
        print(f"The name is {self.name}")
        print(f"The USN is {self.usn}")

# Creating objects for PrintUserDetails class
# Here we are actually passing 3 arguments. The first arg is the object itself which is assigned to self.
obj1 = PrintUserDetails("Varun",  "CS103")
obj2 = PrintUserDetails("Hitesh", "CS065")

# Calling the objects to print details by passing name and usn.
obj1.print_user_details()
obj2.print_user_details()
