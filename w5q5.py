# Write a function for Modular Exponentiation mod_exp(base, exponent, modulus) that efficiently calculates (baseexponent) % modulus.
import time
import tracemalloc
def mod_exp(base, exponent, modulus):
    start_time = time.time()
    tracemalloc.start() 
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:     
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    tracemalloc.stop()
    exec_time = end_time - start_time
    return result, exec_time, current, peak
base = 7
exponent = 256
modulus = 13
value, exec_time, current_mem, peak_mem = mod_exp(base, exponent, modulus)
print(f"Result: {value}")
print(f"Execution Time: {exec_time} seconds")
print(f"Current Memory Usage: {current_mem} bytes")
print(f"Peak Memory Usage: {peak_mem} bytes")
