numbers = [1, 2, 3, 4, 5]

max = numbers[0]

min = numbers[0]

for n in numbers:
    if n > max:
        max = n
    if n < min:
        min = n

print("max: ", max)
print("min: ", min)
