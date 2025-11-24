def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def legendre_symbol(a, p):
    
    exp = (p - 1) // 2
    res = mod_pow(a, exp, p)
    if res == 1:
        return 1
    elif res == p - 1:
        return -1
    else:
        
        return 0
    
print(legendre_symbol(2, 5))  
print(legendre_symbol(3, 5)) 
print(legendre_symbol(4, 5))  
print(legendre_symbol(1, 7)) 
print(legendre_symbol(2, 7))
