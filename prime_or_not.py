n = int(input("enter no: "))
if n < 1:
   print("is not a prime number")
else:
   
   for i in range(2,n):
       if (n % i) == 0:
           print("not prime")
           break
   else:
       print("prime number")