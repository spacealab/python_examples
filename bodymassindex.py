print("body mass index calculation program")
weight = int(input("enter your weight in kg: "))
height = int(input("enter your height in cm: "))
index = weight / (height*weight)

if index <= 18:
    print("you are underweight")
elif index > 18 and index <=25:
    print("you are normal")
elif index > 30:
    print("you are overweight")