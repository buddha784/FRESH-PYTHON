n = int(input("Enter a number: "))
import math

def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1
    return count

print(f"φ({n}) = {euler_totient(n)}")
