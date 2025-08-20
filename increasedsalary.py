NewSalary = 0
Salary = input("input salary")
Raise = input("salary raise rate(%): ")

NewSalary = int(Salary) + (int(Salary) * int(Raise) / 100)
print("increased salary :", NewSalary)
