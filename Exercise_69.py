def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = 45
result = factorial(num)
print(f"The factorial of {num} is {result}")