data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

key = input("Enter the key to check: ")

try:
    value = data[key]
    print(f"The value for '{key}' is: {value}")
except KeyError:
    print(f"Key '{key}' not found in the dictionary.")