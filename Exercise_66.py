def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = int(input("Enter temperature in Celsius: "))
print(convert_to_fahrenheit(celsius))  # Example usage