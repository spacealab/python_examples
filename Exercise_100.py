from functools import reduce

number = [5, 2, 1, 4, 3, 5, 6, 8, 7, 9]

maximum = reduce(lambda a, b: a if a > b else b, number)
print("Maximum value in the list is:", maximum)