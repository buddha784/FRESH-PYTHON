#Write a function Partition Function p(n) partition_function(n) that calculates the number of distinct ways to write n as a sum of positive integers.
import time
import tracemalloc
def partition_function(n):
    p = [0] * (n + 1)
    p[0] = 1  
    for k in range(1, n + 1):
        total = 0
        m = 1
        while True:
            g1 = m * (3*m - 1) // 2
            g2 = m * (3*m + 1) // 2
            if g1 > k:
                break
            sign = -1 if (m % 2 == 0) else 1
            total += sign * p[k - g1]

            if g2 <= k:
                total += sign * p[k - g2]
            m += 1
        p[k] = total
    return p[n]
n = int(input("Enter n: "))
tracemalloc.start()
start = time.time()
result = partition_function(n)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
exec_time = time.time() - start
print(f"\np({n}) = {result}")
print(f"Execution Time: {exec_time:.6f} seconds")
print(f"Memory Used: {peak/1024:.2f} KB")
