def mobius(n):
    if n == 1:
        return 1

    prime_factors = {}
    temp = n
    i = 2

    while i * i <= temp:
        while temp % i == 0:
            prime_factors[i] = prime_factors.get(i, 0) + 1
            temp //= i
        i += 1
    
    if temp > 1:  
        prime_factors[temp] = prime_factors.get(temp, 0) + 1

    
    for count in prime_factors.values():
        if count > 1:
            return 0

    
    if len(prime_factors) % 2 == 0:
        return 1
    else:
        return -1



for n in range(1, 21):
    print(f"μ({n}) = {mobius(n)}")
