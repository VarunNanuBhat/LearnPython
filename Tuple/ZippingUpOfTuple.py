'''
Creating a list of tuples
by combining 2 tuples into 1
using zip()
'''

#Declaring tuples
topics = ("Machine learning", "Android", "Frontend")
langs_used = ("Python", "Java", "ReactJS")
#zipping up 2 tuples to map values
learning_card = zip(topics, langs_used)
print(type(learning_card))
#printing the elements inside learning card
for element in learning_card:
    print(element)
else:
    print("Task completed")




