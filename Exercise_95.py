import re

result = re.fullmatch(r'\w+@\w+\.\w+', "user123gmailcom")

print(result)  # Output: None
