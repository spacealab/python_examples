numbers = [2, 4, 6, 8, 100, 12, 14, 16, 18, 20, 14, 24, 26, 28, 30]

max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print("The maximum number is:", max)