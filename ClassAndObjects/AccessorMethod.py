'''
Program to get the
sum and average of
3 numbers
'''


class FindSumAndAverage:

    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sum_and_avg(self):
        sum = self.num1 + self.num2 + self.num3
        avg = sum/3
        return sum, avg

# Creating 2 objects to find sum and average of 3 numbers
obj1 = FindSumAndAverage(25, 45, 65)
obj2 = FindSumAndAverage(39, 68, 88)

# Printing the results
print(f"The sum and average is {obj1.sum_and_avg()}")
print(f"The sum and average is {obj2.sum_and_avg()}")




