# Write a function is_highly_composite(n) that checks if a number has more divisors than any smaller number.
import math
import time
import sys
import collections
def count_divisors(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    count = 0
    limit = int(math.sqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
    return count
def is_highly_composite(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    divisors_n = count_divisors(n)

    for k in range(1, n):
        divisors_k = count_divisors(k)
        
        if divisors_k >= divisors_n:
            return False
    return True
def run_analysis(n_to_check):
    mem_before = sys.getsizeof(collections.Counter(locals()))
    start_time = time.time()
    is_hcn = is_highly_composite(n_to_check)
    end_time = time.time()
    mem_after = sys.getsizeof(collections.Counter(locals()))
    print(f"\n--- Checking if N = {n_to_check} is Highly Composite ---")
    print(f"Result: {n_to_check} is {'Highly Composite' if is_hcn else 'NOT Highly Composite'}")
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"TIME TAKEN: {elapsed_time_ms:.4f} milliseconds")
    memory_used_bytes = mem_after - mem_before
    print(f"MEMORY USED: {memory_used_bytes} bytes")
    estimated_steps = int(n_to_check * math.sqrt(n_to_check) * 1.5)
    print(f"NO. OF STEPS: ~{estimated_steps:,} operations")
RUN_N = 12
run_analysis(RUN_N)
