# Write a function chinese Remainder Theorem Solver crt(remainders, moduli) that solves a system of congruences x ≡ ri mod mi.
import math
import time
import tracemalloc
import sys
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)
def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse does not exist (moduli must be pairwise coprime).")
    return x % m
def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        raise ValueError("Remainders and moduli lists must have the same length.")
    M = 1
    for m in moduli:
        M *= m
    result = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        inv = mod_inverse(Mi, m)
        result += r * Mi * inv
    return result % M
remainders = [2, 3, 2]
moduli = [3, 5, 7]
start_time = time.perf_counter()
x = crt(remainders, moduli)
end_time = time.perf_counter()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"## CRT Calculation Result")
print(f"x = {x}")
print("---")
print(f"## Time Taken")
time_taken_seconds = end_time - start_time
print(f"**Execution Time (Wall Time):** {time_taken_seconds * 1e6:.3f} microseconds (µs)")
print("---")
print(f"## Memory Used")
print(f"**Peak Memory Usage:** {peak_memory / 1024:.2f} KiB")
print(f"**Current Memory Usage:** {current_memory / 1024:.2f} KiB")
