# Write a function Quadratic Residue Check is_quadratic_residue(a, p) that checks if x2 ≡ a mod p has a solution.
import time
import sys
import math
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
def is_quadratic_residue(a: int, p: int) -> bool:
    if not isinstance(a, int) or not isinstance(p, int):
        raise ValueError("Inputs 'a' and 'p' must be integers.")   
    if p < 1:
        raise ValueError("Modulus 'p' must be a positive integer.")
    if p == 1:
        return True      
    if p == 2:
        return True
    if not is_prime(p):
        raise ValueError("Euler's Criterion requires 'p' to be a prime number.")
    a_mod_p = a % p
    if a_mod_p == 0:
        return True     
    exponent = (p - 1) // 2 
    result = pow(a_mod_p, exponent, p) 
    if result == 1:
        return True
    if result == p - 1:
        return False
    return False
if __name__ == "__main__":
    TEST_A = 10
    TEST_P = 13
    print(f"--- Running Quadratic Residue Check: x^2 ≡ {TEST_A} (mod {TEST_P}) ---")
    start_time = time.perf_counter()
    try:
        is_residue = is_quadratic_residue(TEST_A, TEST_P)
    except ValueError as e:
        is_residue = f"Error: {e}"
    end_time = time.perf_counter()
    if isinstance(is_residue, bool):
        num_steps = math.ceil(math.log2(TEST_P - 1)) if TEST_P > 2 else 1
        print(f"\n1. Number of Steps (Modular Exponentiation Cycles): {num_steps}")
    else:
        print("\n1. Number of Steps: N/A (Error Occurred)")
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"2. Time Taken (Execution Time): {elapsed_time_ms:.6f} milliseconds")
    input_memory_a = sys.getsizeof(TEST_A)
    input_memory_p = sys.getsizeof(TEST_P)
    output_memory = sys.getsizeof(is_residue)
    print(f"\n3. Memory Used (Bytes):")
    print(f"   - Input A ({TEST_A}): {input_memory_a} bytes")
    print(f"   - Input P ({TEST_P}): {input_memory_p} bytes")
    print(f"   - Result ({is_residue}): {output_memory} bytes")
    print("\n--- Final Result ---")
    if isinstance(is_residue, bool):
        print(f"Is {TEST_A} a quadratic residue modulo {TEST_P}? -> {is_residue}")
    else:
        print(is_residue)
