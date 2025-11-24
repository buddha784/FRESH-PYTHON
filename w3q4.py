# Write a function is_pronic(n) that checks if a number is the product of two consecutive integers.
import math
def is_pronic(n: int) -> bool:
    if n < 0:
        return False    
    if n == 0:
        return True        
    k = int(math.sqrt(n))    
    return k * (k + 1) == n
pronic_numbers = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
not_pronic_numbers = [1, 3, 4, 5, 7, 10, 11, 13, 14, 15]
test_results = {}
for num in pronic_numbers:
    test_results[num] = is_pronic(num)
for num in not_pronic_numbers:
    test_results[num] = is_pronic(num)
print("--- Pronic Number Test Results ---")
for num, is_p in sorted(test_results.items()):
    if is_p:
        k = int(math.sqrt(num))
        print(f"Number {num}: {is_p} ({k} * {k+1})")
    else:
        print(f"Number {num}: {is_p}")
print("\nTesting edge case n=100:")
print(f"is_pronic(100): {is_pronic(100)}")
