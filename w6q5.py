#Write a function Fibonacci Prime Check is_fibonacci_prime(n) that checks if a number is both Fibonacci and prime import time
import sys
import math
class PerformanceMetrics:
    def __init__(self):
        self.steps = "O(sqrt(n))"
        self.time_ns = 0
        self.memory_bytes = 0
        self.result = None
        self.n = None
    def calculate_metrics(self, func, n):
        self.n = n
        start_time = time.perf_counter_ns()
        self.result = func(n)
        end_time = time.perf_counter_ns()
        self.time_ns = end_time - start_time
        n_size = sys.getsizeof(n)
        result_size = sys.getsizeof(self.result)
        self.memory_bytes = n_size + result_size
        self.steps = "O(sqrt(n))"
        return self.result
def is_fibonacci(n):
    if n < 0:
        return False
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
def is_fibonacci_prime(n):
    if not is_prime(n):
        return False
    return is_fibonacci(n)
N_TEST_1 = 13 
print(f"--- Checking Fibonacci Prime Property ---")
print(f"\nChecking N = {N_TEST_1}")
metrics_1 = PerformanceMetrics()
final_result_1 = metrics_1.calculate_metrics(is_fibonacci_prime, N_TEST_1)
print(f"Result: {'YES, it is a Fibonacci Prime' if final_result_1 else 'NO, it is not a Fibonacci Prime'}")
print("\n--- Performance Metrics (N=13) ---")
print(f"Test Case: n={metrics_1.n}")
print(f"1. Steps/Time Complexity: {metrics_1.steps}")
print(f"   (This is due to the primality test up to sqrt(n).)")
print(f"2. Time Taken (Approx.): {metrics_1.time_ns / 1000:.3f} microseconds")
print(f"   ({metrics_1.time_ns} nanoseconds)")
print(f"3. Memory Used (Approx.): {metrics_1.memory_bytes} bytes")
print(f"   (This measures the storage size of inputs and output.)")
