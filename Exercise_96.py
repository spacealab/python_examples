import re

result = re.findall(r'\d+', 'Room is 123 and code is 4567')

print(result)  # Output: ['123', '4567']