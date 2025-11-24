#Write a function Carmichael Number Check is_carmichael(n) that checks if a composite number n satisfies an−1 ≡ 1 mod n for all a coprime to n.
import time
def power_with_modulo(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2        
    return result
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False        
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6    
    return True
def gcd(a, b):
    while b:    
        a, b = b, a % b     
    return a
def is_carmichael(n):
    if is_prime(n):
        return False
    for a in range(2, n):
        if gcd(a, n) == 1:
            if power_with_modulo(a, n - 1, n) != 1:
                return False
    return True
number_to_check = 561 
start_time = time.time()
if is_carmichael(number_to_check):
    print(f"{number_to_check} is a Carmichael number.")
else:
    print(f"{number_to_check} is not a Carmichael number (or is prime).")
end_time = time.time()
execution_time = end_time - start_time
print(f"Time of execution: {execution_time:.6f} seconds")
