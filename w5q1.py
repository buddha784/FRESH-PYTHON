# Write a function aliquot_sum(n) that returns the sum of all proper divisors of n (divisors less than n).
import time
def aliquot_sum(n):
    if n == 1:
        return 0
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i * i != n:
                sum_div += n // i                
    return sum_div
num = 30  
start_time = time.time()
result = aliquot_sum(num)
end_time = time.time()
print(f"The number is: {num}")
print(f"The sum of proper divisors (aliquot sum) is: {result}")
print(f"Time of execution: {end_time - start_time:.6f} seconds")
