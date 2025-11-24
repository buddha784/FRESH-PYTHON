# Write a function count_distinct_prime_factors(n) that returns how many unique prime factors a number has.
import time
import sys
def prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
        
    if n > 2:
        factors.append(n)
        
    return factors
def count_distinct_prime_factors(n):
    factors = prime_factors(n)
    return len(set(factors))
def analyze_execution(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    time_taken_ms = (end_time - start_time) * 1000
    memory_used_bytes = sys.getsizeof(result)
    return result, time_taken_ms, memory_used_bytes
number = 100
distinct_count, time_ms_distinct, memory_bytes_distinct = analyze_execution(count_distinct_prime_factors, number)
print(f"The number of distinct prime factors of {number} is: {distinct_count}")
print(f"Execution Time: {time_ms_distinct:.6f} milliseconds")
print(f"Memory Used (Result Object): {memory_bytes_distinct} bytes")
