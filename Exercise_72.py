def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
        
safe_division(10, 2)  # Should print: Result: 5.0
safe_division(10, 0)  # Should print: Error: Division by zero
