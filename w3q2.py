# Write a function for harshad number is_harshad(n) that checks if a number is divisible by the sum of its digits.
import time
import tracemalloc
def is_harshad(n):
    digits_sum = sum(int(digit) for digit in str(n))
    return n % digits_sum == 0 if digits_sum != 0 else False
def test_harshad_numbers():
    test_numbers = [18, 19, 21, 1729, 123, 6804, 0]
    for num in test_numbers:
        print(f"{num} is Harshad: {is_harshad(num)}")
tracemalloc.start()
start_time = time.time()
test_harshad_numbers()
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Current Memory Usage: {current / 1024:.2f} KB")
print(f"Peak Memory Usage: {peak / 1024:.2f} KB")
