'''
Program to check if a user is
eligible to vote or not with the
help of getters and setters
'''

class EligibleForVoting:

    def __init__(self, age = 0):
        self._age = age

    # This method will return the age of the user.
    def get_age(self):
        return self._age

    # This method only set the age of user if it is >18 else the age will be set to 0.
    def set_age(self, age):
        if (age >= 18):
            self._age = age

# Creating 2 objects for class EligibleForVoting
varun = EligibleForVoting()
hitesh = EligibleForVoting()

# Invoking the setters for < 18 and > 18 condition
varun.set_age(12)
hitesh.set_age(25)

# Invoking the getters to get the age of the users set.
print(varun.get_age())
print(hitesh.get_age())
