#Write a function zeta_approx(s, terms) that approximates the Riemann zeta function ζ(s) using the first 'terms' of the series.
import time
import sys
import math
def zeta_approx(s: float, terms: int) -> float:
    if s <= 1.0:
        raise ValueError("The series approximation is only valid for s > 1.")
    if terms <= 0:
        return 0.0
    result = 0.0
    for k in range(1, terms + 1):
        term = 1.0 / (k ** s)
        result += term    
    return result
def run_zeta_approx_with_metrics(s: float, terms: int):
    print(f"--- Riemann Zeta Approximation (s={s}, Terms={terms}) ---")    
    try:
        start_time = time.perf_counter()   
        approximation = zeta_approx(s, terms) 
        end_time = time.perf_counter()
        time_taken = (end_time - start_time) * 1000 
        memory_used_bytes = sys.getsizeof(approximation)     
        steps = terms
        print(f"Approximation ζ({s}): {approximation:.10f}")
        if s == 2.0:
            theoretical_value = (math.pi**2) / 6
            error = abs(theoretical_value - approximation)
            print(f"Theoretical Value (ζ(2)): {theoretical_value:.10f}")
            print(f"Absolute Error: {error:.10f}")
        print("\n--- Performance Metrics ---")
        print(f"No. of Terms: {terms}")
        print(f"Time Taken: {time_taken:.6f} milliseconds")
        print(f"Memory Used (Size of Result Float): {memory_used_bytes} bytes")
        print(f"No. of Steps (Loop Iterations/Additions): {steps}")
    except ValueError as e:
        print(f"ERROR: {e}")
if __name__ == "__main__":
    run_zeta_approx_with_metrics(s=2.0, terms=100)
    print("\n" + "="*70 + "\n")
    
    run_zeta_approx_with_metrics(s=3.0, terms=1000)
    print("\n" + "="*70 + "\n")
