number = int(input("Enter a number: "))

number = abs(number)

count = 0
temp = number

if number == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1
print("The number of digits in the number is:", count)