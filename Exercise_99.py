import re

result = re.findall(r'\b\w+ing\b', "I am learning coding and cooking.")

print(result)  # ['learning', 'coding', 'cooking']

