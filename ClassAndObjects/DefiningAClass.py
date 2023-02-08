'''
Defining a class
to print "Hello World!!"
'''

class PrintHelloWorld:
    # Functions inside class to replicate the behavior of object.

    def print_hello_world(self):
        print("Hello World!!")


# Creating the objects for class "PrintHelloWorld"
obj1 = PrintHelloWorld()
obj2 = PrintHelloWorld()

# Calling the object obj to pint "Hello World!!"
# In the below case, object is passed as a parameter, hence self keyword will refer to the object itself. 
obj1.print_hello_world()
obj2.print_hello_world()
