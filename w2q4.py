# Write a function digital_root(n) that repeatedly sums the digits of a number until a single digit is obtained.
import time
def digital_root(n):
    iterations = 0
    start_time = time.time()   
    while n >= 10:   
        s = 0
        temp = n
        while temp > 0:  
            s += temp % 10
            temp //= 10
        n = s
        iterations += 1
    end_time = time.time()   
    execution_time = end_time - start_time
    print("Digital root:", n)
    print("Iterations:", iterations)
    print("Execution time:", execution_time, "seconds")
    return n
