def divisor_sum(n):   
    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

n = int(input("Enter a positive integer: "))
result = divisor_sum(n)   
print(f"The sum of all divisors of {n} is {result}.")

