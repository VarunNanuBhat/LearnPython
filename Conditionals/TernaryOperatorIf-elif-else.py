'''
program to understand concept of ternary operator
for if-elif-else
'''


#Accpet marks from user
marks = int(input("Enter marks of student: "))
print("Distinction") if marks > 70 else print("FC") if marks > 50 else print("SC") if marks > 35 else print("Fail")


