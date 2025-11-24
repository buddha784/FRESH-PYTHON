#Write a function Lucas Numbers Generator lucas_sequence(n) that generates the first n Lucas numbers (similar to Fibonacci but starts with 2,1).
import time
import sys
import collections
def lucas_sequence(n: int) -> list[int]:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")
    if n == 0:
        return []
    if n == 1:
        return [2]
    if n == 2:
        return [2, 1]
    sequence = [2, 1]
    for _ in range(2, n):
        next_lucas = sequence[-1] + sequence[-2]
        sequence.append(next_lucas)
    return sequence
def run_lucas_sequence_with_metrics(n: int):
    start_time = time.perf_counter()   
    lucas_nums = lucas_sequence(n)   
    end_time = time.perf_counter()
    time_taken = (end_time - start_time) * 1000 
    memory_used_bytes = sys.getsizeof(lucas_nums)    
    steps = max(0, n - 2) 
    print(f"--- Lucas Sequence (First {n} Numbers) ---")
    print(lucas_nums)
    print("\n--- Performance Metrics ---")
    print(f"N: {n} terms")
    print(f"Time Taken: {time_taken:.6f} milliseconds")
    print(f"Memory Used: {memory_used_bytes} bytes (Size of the output list)")
    print(f"No. of Steps (Main Loop Iterations): {steps}")
if __name__ == "__main__":
    run_lucas_sequence_with_metrics(n=10)
    print("\n" + "="*50 + "\n")
    run_lucas_sequence_with_metrics(n=20)
