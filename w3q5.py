# Write a function prime_factors(n) that returns the list of prime factors of a number.
import time
import tracemalloc
def prime_factors(n):
    tracemalloc.start()
    start_time = time.time()
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    memory_used = peak / 1024  
    print("\nPrime factors:", factors)
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Peak memory usage: {memory_used:.2f} KB")
n = int(input("Enter a number: "))
prime_factors(n)
