# Write a function is_mersenne_prime(p) that checks if 2p - 1 is a prime number (given that p is prime).
import time
import tracemalloc
def is_mersenne_prime(p: int) -> bool:
    
    if p == 2:
        return True  
    if p < 2:
        return False

    M = (1 << p) - 1  
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M
    return s == 0
p = 7
start_time = time.time()
tracemalloc.start()
result = is_mersenne_prime(p)
current, peak = tracemalloc.get_traced_memory()
end_time = time.time()
tracemalloc.stop()
print(f"Is 2^{p} - 1 a Mersenne Prime? : {result}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Current Memory Usage: {current / 1024:.3f} KB")
print(f"Peak Memory Usage: {peak /1024:.3f} KB")
