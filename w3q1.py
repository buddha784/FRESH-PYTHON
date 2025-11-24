# Write a function is_deficient(n) that returns True if the sum of proper divisors of n is less than n.
import time
def is_deficient(n):
    start_time = time.time()
    iterations = 0
    if n <= 1:
        end_time = time.time()
        return False, iterations, end_time - start_time    
    divisor_sum = 0
    i = 1
    while i * i <= n:
        iterations += 1
        if n % i == 0:
            if i != n:
                divisor_sum += i          
            other_divisor = n // i
            if other_divisor != n and other_divisor != i:
                divisor_sum += other_divisor        
        i += 1  
    end_time = time.time()
    execution_time = end_time - start_time
    return divisor_sum < n, iterations, execution_time
number = 12
is_def, iterations, exec_time = is_deficient(number)
print(f"Number: {number}")
print(f"Is deficient: {is_def}")
print(f"Iterations: {iterations}")
print(f"Execution time: {exec_time:.8f} seconds")
