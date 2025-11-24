# Implement pollard_rho(n) for integer factorization using Pollard's rho algorithm.
import random
import math
import time
import tracemalloc
def pollard_rho(n):
    if n % 2 == 0:
        return 2, 1
    def f(x, c):
        return (x * x + c) % n
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    steps = 0
    while d == 1:
        steps += 1     
        x = f(x, c)       
        y = f(f(y, c), c)
        d = math.gcd(abs(x - y), n)
        if d == n:
            new_factor, new_steps = pollard_rho(n)
            return new_factor, steps + new_steps           
    return d, steps
if __name__ == "__main__":
    n = 8051   
    print(f"--- Starting Factorization of N={n} ---")
    tracemalloc.start()
    start_time = time.time()
    factor, steps = pollard_rho(n)       
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\n--- Results ---")
    print(f"Number to factorize (n): {n}")
    print(f"A factor of {n} is: {factor}")
    print(f"Number of Steps/Iterations: {steps}")
    print(f"Execution Time: {(end_time - start_time):.10f} seconds")
    print(f"Memory Usage: {current / 1024:.4f} KB")
    print(f"Peak Memory Usage: {peak / 1024:.4f} KB")
