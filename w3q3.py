import time
import tracemalloc
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))
start_time = time.time()
tracemalloc.start()
num = int(input("Enter a number: "))
if is_automorphic(num):
    print(num, "is an automorphic number.")
else:
    print(num, "is not an automorphic number.")
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.10f} seconds")
print(f"Current Memory Usage: {current / 1024:.3f} KB")
print(f"Peak Memory Usage: {peak / 1024:.3f} KB")
