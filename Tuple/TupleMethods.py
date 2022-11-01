'''
Demonstrating the various tuple methods
'''

my_tuple = (1, 2.0, 'c', "strings")
#count() - Returns the count of the specified element.
count_of_a = my_tuple.count('c')
print(f"The count of \"c\" in tuple is \"{count_of_a}\"")
#index() - returns the index value of the specified element.
print(f"The index value of \"2.0\" is \"{my_tuple.index(2.0)}\"")


