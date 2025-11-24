# Write a function multiplicative_persistence(n) that counts how many steps until a number's digits multiply to a single digit.
import time
import sys
import mat
def calculate_digit_product(n):
    if n < 0:
        n = abs(n)        
    product = 1
    for digit_char in str(n):
        product *= int(digit_char)
    return product
def multiplicative_persistence(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    current_number = n
    steps = 0    
    while current_number > 9:
        steps += 1
        current_number = calculate_digit_product(current_number)        
    return steps
if __name__ == "__main__":
    TEST_NUMBER = 77    
    print(f"--- Running Multiplicative Persistence for N = {TEST_NUMBER} ---")  
    start_time = time.perf_counter()   
    persistence_result = multiplicative_persistence(TEST_NUMBER)   
    end_time = time.perf_counter()   
    print(f"\n1. Number of Steps (Multiplicative Persistence): {persistence_result}")
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"2. Time Taken (Execution Time): {elapsed_time_ms:.6f} milliseconds")
    input_memory = sys.getsizeof(TEST_NUMBER)
    output_memory = sys.getsizeof(persistence_result)
    print(f"\n3. Memory Used (Bytes):")
    print(f"   - Input Number ({TEST_NUMBER}): {input_memory} bytes")
    print(f"   - Resulting Steps ({persistence_result}): {output_memory} bytes")
    if TEST_NUMBER <= 999:
        print("\n--- Step Breakdown ---")
        n_current = TEST_NUMBER
        step = 0
        while n_current > 9:
            step += 1
            product = calculate_digit_product(n_current)
            print(f"Step {step}: {n_current} -> {list(str(n_current))} -> Product: {product}")
            n_current = product
        print(f"Final Result: Single digit {n_current} reached in {step} steps.")
