num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    result = int(num1) + int(num2)
    print("The sum is:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")