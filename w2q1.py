import time
n=int(input("enter a number:"))
start= time.time()
t=1
for i in range(1,n+1):
    t*=i
end=time.time()
print("factorial of" ,n,"=",t)
execution_time =end-start
print("execution time:",execution_time,"seconds")
divisors=0
for i in range(1, n + 1):
    if n % i == 0:
        divisors += 1
memory_used = divisors * 28  
print("Memory used (approx):", memory_used,"bytes")
