import re 

result = re.fullmatch(r'03\d{9}', "03987654321")

print(result)  # <re.Match object; span=(0, 11), match='03987654321'>