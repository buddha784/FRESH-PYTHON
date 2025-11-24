# Implement the probabilistic Miller-Rabin test is_prime_miller_rabin(n, k) with k rounds.
import time
import random
def is_prime_miller_rabin(n, k=20):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue  
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break  
        else:
            return False
    return True
number_to_test = 100000007 
rounds = 20 
start_time = time.time()
is_prime_1 = is_prime_miller_rabin(number_to_test, rounds)
end_time = time.time()
print(f"Testing number: {number_to_test} with {rounds} rounds.")
print(f"Is {number_to_test} prime? {'Yes, probably' if is_prime_1 else 'No, it is composite'}")
print(f"Time of execution: {end_time - start_time:.6f} seconds")
