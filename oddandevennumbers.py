NumList = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    NumList.append(value)
    
for j in range(Number) :
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]

print("\nThe Sum of Even Numbers is : ", Even_Sum)
print("\nThe Sum of Odd Numbers is : ", Odd_Sum)
