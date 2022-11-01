'''
Chatbot using if-elif-else ladder
'''

#Introductory statements for chatbot
#to interact with user
print("Hello, Welcome to chat bot service")
print("How may I help you?")
print()
print("Hit 1 for software installation request")
print("Hit 2 for software update request")
print("Hit 3 for laptop service request")
print("Hit 4 for others")
#Accept input from user
userInput = int(input())
#Apply conditionals and perform the necessary tasks
if userInput == 1:
    softwareNeeded = input("Enter the name of software needed: ")
elif userInput == 2:
    softwareUpdate = input("Enter the name of software to be updated: ")
elif userInput == 3:
    laptopBrand = input("Enter the brand of laptop to be service: ")
else:
    otherRequest = input("Enter the request to be fulfilled: ")
#end of if-elif-else
print("Thank you for contacting chat bot service. Our team will reach out to you shortly.")

