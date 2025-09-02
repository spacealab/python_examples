text = input("Enter some text: ")

if len(text) > 0 and text[0] != "0":
    print("The text is not empty and does not start with '0'.")
    print("The first character is:", text[0])
else:
    print("The text is either empty or starts with '0'.")