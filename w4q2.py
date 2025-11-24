#Write a function is_prime_power(n) that checks if a number can be expressed as pk where p is prime and k ≥ 1.
import time
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
def is_prime_power(n):
    if n <= 1:
        return False
    for p in range(2, int(n**0.5) + 1):
        if is_prime(p):
            power = p
            while power <= n:
                if power == n:
                    return True
                power *= p
    return is_prime(n)
start = time.time()
num = int(input("Enter number: "))
result = is_prime_power(num)
end = time.time()
print("Is prime power:", result)
print("Execution time:", (end - start),"seconds")
