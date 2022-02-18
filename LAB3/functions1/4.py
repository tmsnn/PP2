def filter_prime(l):
    primes = []
    for i in l:
        filter_prime = True
        for el in range(2, int(i ** 0.5) + 1):
            if i % el == 0:
                filter_prime = False
                break
        if filter_prime == True:
            primes.append(i)
    print(f"Prime numbers in list:")
    print(*primes)
    
l = list(map(int, input().split()))
filter_prime(l)