B=int(input("enter your no."))
prime_count = 0
for num in range (0,B+1):
 if num > 1:
   for i in range (2,num):
      if num % i == 0:
         break
   else: 
        print(num) 
        prime_count +=1 
print("no. of prime before", prime_count )        
