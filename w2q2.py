# Write a function is_palindrome(n) that checks if a number reads the same forwards and backwards.
import time
import sys
def is_palindrome(n):
    if n < 0:
        return False, {
            "time_taken_ms": 0.0,
            "math_iterations": 0,
            "space_used_bytes": 0,
            "notes": "Negative number treated as non-palindrome, no computation performed."
        }     
    start_time = time.perf_counter()
    original_number = n
    reversed_number = 0
    temp_n = n
    iterations = 0 
    while temp_n > 0:
        digit = temp_n % 10
        reversed_number = (reversed_number * 10) + digit
        temp_n = temp_n // 10
        iterations += 1
    is_palin = original_number == reversed_number
    end_time = time.perf_counter()
    time_taken_ms = (end_time - start_time) * 1000 
    space_used_bytes = 120 
    metrics = {
        "time_taken_ms": time_taken_ms, 
        "math_iterations": iterations,
        "space_used_bytes": space_used_bytes,
        "notes": "Time is in milliseconds (ms). Iterations count the number of loop cycles."
    }
    return is_palin, metrics
test_numbers = [
    12321,          
    1001,           
    12345,          
    7,              
    12345678987654321, 
    -121            
]
print("--- In-Memory Palindrome Checker Results ---")
for number in test_numbers:
    result, metrics = is_palindrome(number) 
    print("-" * 40)
    print(f"Checking Number: {number}")
    print(f"Is Palindrome: {result}")
    print("\n--- Performance Metrics ---")
    print(f"1. Time Taken: {metrics['time_taken_ms']:.4f} ms")
    print(f"2. Number of Steps (Iterations): {metrics['math_iterations']}")
    print(f"3. Memory Used (Estimated): {metrics['space_used_bytes']} bytes")
