password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
elif len(password) > 16:
    print("Password is too long. It must be no more than 16 characters long.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
else:
    print("Password is valid.")