number = int(input("Enter the number: "))

if number < 2:
    print(f"{number} is not prime.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")