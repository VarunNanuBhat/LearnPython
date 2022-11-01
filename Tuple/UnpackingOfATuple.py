'''
Unpacking of a tuple
inside a list
using looping
'''

# Declaring a tuple inside a list
my_list = [("Machine learning", "Python"), ("Android", "Java"), ("Frontend", "ReactJS")]
# Looping through each elements inside them
for topic, subject in my_list:
    print(f"{subject} is used for {topic}")
else:
    print("Task completed")



