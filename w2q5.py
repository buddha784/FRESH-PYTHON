# Write a function is_abundant(n) that returns True if the sum of proper divisors of n is greater than n.
n=int(input("n: "))
f=1
for i in range(2,n+1): f*=i
s=str(n); pal = s==s[::-1]
d=[int(c) for c in s if c.isdigit()]; mean=sum(d)/len(d)
dr=abs(n)
while dr>9: dr=sum(int(c) for c in str(dr))
sd=0
if n>1:
    sd=1
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sd+=i
            if i!=n//i: sd+=n//i
abundant = sd>n
print("factorial =",f)
print("is_palindrome =",pal)
print("mean_of_digits =",mean)
print("digital_root =",dr)
print("is_abundant =",abundant)
