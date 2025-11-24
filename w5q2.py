# Write a function are_amicable(a, b) that checks if two numbers are amicable (sum of proper divisors of a equals b and vice versa).
import time
import tracemalloc
def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
def are_amicable(a, b):
    return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a
a = 220
b = 284
tracemalloc.start()
start_time = time.time()
result = are_amicable(a, b)
current, peak = tracemalloc.get_traced_memory()
end_time = time.time()
tracemalloc.stop()
print(f"Are {a} and {b} amicable? -> {result}")
print(f"Execution Time: {(end_time - start_time):.10f} seconds")
print(f"Memory Usage: {current / 1024:.4f} KB")
print(f"Peak Memory Usage: {peak / 1024:.4f} KB")
