like = input("Do you like Python? (yes/no): ").strip().lower()
if like == "yes":
    like = True
    print("That's great to hear!")
else:
    like = False
    print("Oh, that's too bad.")