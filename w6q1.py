#Write a function Modular Multiplicative Inverse mod_inverse(a, m) that finds the number x such that (a * x) ≡ 1 mod m.
import time
def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m  
        a = t      
        t = y
        y = x - q * y
        x = t
    if m != 1:
        return None
    if x < 0:
        x += m0       
    return x
val_a = 3
val_m = 11
start_time = time.time()
inverse_result = mod_inverse(val_a, val_m)
end_time = time.time()
print(f"Finding the modular multiplicative inverse of {val_a} mod {val_m}:")
if inverse_result is not None:
    print(f"The inverse x is: {inverse_result}")
    print(f"Verification: ({val_a} * {inverse_result}) % {val_m} == {(val_a * inverse_result) % val_m}")
else:
    print(f"Inverse does not exist for {val_a} mod {val_m} (GCD is not 1).")
print(f"Time of execution: {end_time - start_time:.6f} seconds")
