def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
n = int(input("Enter a number: "))
print(is_even(n))