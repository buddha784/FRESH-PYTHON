# Write a function Polygonal Numbers polygonal_number(s, n) that returns the n-th s-gonal number.
import time
import tracemalloc
import sys
def polygonal_number(s, n):
    return ((s - 2) * n * n - (s - 4) * n) // 2
if __name__ == "__main__":
    examples = [
        (3, 5, "Triangular"),
        (4, 5, "Square"),
        (5, 5, "Pentagonal")
    ]
    tracemalloc.start()
    start_time = time.time() 
    steps = 0
    results = []
    for s, n, shape in examples:
        result = polygonal_number(s, n)
        results.append((shape, s, n, result))
        steps += 1
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"--- Polygonal Number Calculation (n=5) ---")
    for shape, s, n, result in results:
        print(f"{shape} Number (s={s}): {result}")      
    print("\n--- Performance Metrics ---")
    print(f"Total Function Calls (Steps): {steps}")
    print(f"Execution Time: {(end_time - start_time):.10f} seconds")
    print(f"Memory Usage: {current / 1024:.4f} KB")
    print(f"Peak Memory Usage: {peak / 1024:.4f} KB")
