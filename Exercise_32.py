text = input("Enter some text: ")

if len(text) != 1:
    print("Error: Please enter a single character.")
new_text = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if text in new_text:
    print("Vowel")
else:
    print("Consonant")