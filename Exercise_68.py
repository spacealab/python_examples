def get_min_max(numbers):    
    if not numbers:
        return None, None
    else:
        return min(numbers), max(numbers)
    
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_value, max_value = get_min_max(numbers)
print(f"Minimum: {min_value}, Maximum: {max_value}")