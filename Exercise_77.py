filename = 'try.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")