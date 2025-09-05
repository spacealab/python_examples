for i in range(2, 51):
    is_prime = True
    for i in range(2, int(i**0.5) + 1):
        if i % i == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')