try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("The result of the division is:", result)

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
